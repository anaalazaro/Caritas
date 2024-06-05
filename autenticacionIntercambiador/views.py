from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from .models import Intercambiador
from .forms import LoginForm
import random

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            dni = form.cleaned_data['dni']
            password = form.cleaned_data['password']

            user = authenticate(request, username=dni, password=password)

            # Escenario 1: Inicio de sesión exitoso
            if user is not None and not user.is_blocked:
                login(request, user)
                return HttpResponse("Inicio de sesión exitoso")

            # Escenario 2 y 3: Fallos por usuario inexistente o contraseña incorrecta
            else:
                # Intento de usuario inexistente
                if not Intercambiador.objects.filter(dni=dni).exists():
                    return HttpResponse("El usuario y/o la contraseña son incorrectos")

                # Intento con usuario existente pero contraseña incorrecta
                user_instance = Intercambiador.objects.get(dni=dni)
                user_instance.failed_login_attempts += 1

                # Escenario 4: Bloqueo por múltiples intentos fallidos
                if user_instance.failed_login_attempts >= 3:
                    user_instance.is_blocked = True
                    user_instance.failed_login_attempts = 0

                    # Generar una contraseña temporal y enviar correo
                    temp_password = str(random.randint(100000, 999999))
                    user_instance.set_password(temp_password)
                    user_instance.motivo_bloqueo = "Demasiados intentos de inicio de sesión fallidos."
                    user_instance.save()

                    # Enviar correo
                    send_mail(
                        'Cuenta Bloqueada',
                        f'Su cuenta ha sido bloqueada. Use esta contraseña para iniciar sesión: {temp_password}. Siga las instrucciones enviadas por correo para desbloquear su cuenta.',
                        'ingecaritas@gmail.com',
                        [user_instance.email],
                        fail_silently=False,
                    )

                    mensaje = f"Su cuenta está bloqueada. Motivo: {user_instance.motivo_bloqueo}"
                    return HttpResponse(mensaje)

                user_instance.save()
                return HttpResponse("El usuario y/o la contraseña son incorrectos")

    # Escenario 5: Usuario bloqueado
    else:
        form = LoginForm()
        return render(request, 'autenticacionIntercambiador/login.html', {'form': form})
