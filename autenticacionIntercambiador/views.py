from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from app.models import CustomUser
from .forms import LoginForm
import random
from django.contrib import messages

def mostrar(request):
    return render(request, 'menuPrincipal.html', {'user': CustomUser})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            dni = form.cleaned_data['dni']
            password = form.cleaned_data['password']

            # Verificar si el usuario existe
            if CustomUser.objects.filter(dni=dni).exists():
                user_instance = CustomUser.objects.get(dni=dni)
                
                # Verificar si el usuario está bloqueado
                if user_instance.is_blocked:
                    error_message = f"Su cuenta está bloqueada. Motivo: {user_instance.motivo_bloqueo}"
                    return render(request, 'autenticacionIntercambiador/login.html', {'form': form, 'error_message': error_message})

                # Autenticar al usuario
                user = authenticate(request, username=dni, password=password)
                if user is not None:
                    if user.roles != 'usuario':
                        error_message = 'No se encuentra habilitado para iniciar sesión por este medio. Elija la opción "Iniciar sesión como administrador o ayudante".'
                        return render(request, 'autenticacionIntercambiador/login.html', {'form': form, 'error_message': error_message})
                    
                    login(request, user)
                    
                    if user.passChange:
                        return redirect('change_desired_password')
                    return redirect('menuPrincipal')
                else:
                    # Incrementar intentos fallidos si la autenticación falla
                    user_instance.failed_login_attempts += 1
                    user_instance.save()

                    if user_instance.failed_login_attempts >= 3:
                        user_instance.is_blocked = True
                        # temp_password = str(random.randint(100000, 999999))
                        # user_instance.set_password(temp_password)
                        user_instance.motivo_bloqueo = "Demasiados intentos de inicio de sesión fallidos."
                        user_instance.save()
                        # send_mail(
                        #     'Cuenta Bloqueada',
                        #     f'Su cuenta ha sido bloqueada. Use esta contraseña temporal para iniciar sesión: {temp_password}. Siga las instrucciones enviadas por correo para desbloquear su cuenta.',
                        #     'ingecaritas@gmail.com',
                        #     [user_instance.email],
                        #     fail_silently=False,
                        # )
                        messages.error(request, f"Su cuenta está bloqueada. Motivo: {user_instance.motivo_bloqueo}")
                        return redirect('change_password')
                    else:
                        error_message = "El usuario y/o la contraseña son incorrectos"
                    
                    return render(request, 'autenticacionIntercambiador/login.html', {'form': form, 'error_message': error_message})
            else:
                error_message = "El usuario y/o la contraseña son incorrectos"
                return render(request, 'autenticacionIntercambiador/login.html', {'form': form, 'error_message': error_message})
    else:
        form = LoginForm()

    return render(request, 'autenticacionIntercambiador/login.html', {'form': form})
