
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from autenticacionIntercambiador.models import Intercambiador
from autenticacionIntercambiador.models import LoginForm
from .forms import CustomUserCreationForm




def hello(request):
    return render(request, 'inicio.html')


def registro(request):
    data = {'form': CustomUserCreationForm()}

    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)

        if user_creation_form.is_valid():
            telefono = user_creation_form.cleaned_data['telefono']
            # Verificar si el número de teléfono es de La Plata y Argentina
            if not telefono.startswith('221'):
                # Si el número de teléfono no es válido, añadir un mensaje de error al formulario
                user_creation_form.add_error('telefono', 'El teléfono debe corresponder a La Plata')
            else:
                # Si el formulario es válido, guardar el usuario y autenticarlo
                user_creation_form.save()
                username = user_creation_form.cleaned_data['dni']
                password = user_creation_form.cleaned_data['password1']
                user = authenticate(request, username=username, password=password)
                login(request, user)
                return redirect('http://127.0.0.1:8000/')  # Redirigir al usuario a la página de inicio

        # Si el formulario no es válido, actualizar los datos con el formulario y sus errores
        data['form'] = user_creation_form

    return render(request, 'registro/registroUsuario.html', data)
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            dni = form.cleaned_data['dni']
            password = form.cleaned_data['password']

            user = authenticate(request, username=dni, password=password)

            # Escenario 1: Inicio de sesión exitoso
            if user is not None:
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

                
                user_instance.save()
                return HttpResponse("El usuario y/o la contraseña son incorrectos")


@login_required  # Asegura que solo usuarios autenticados puedan acceder
def view_profile(request):
    # Obtenemos el usuario autenticado
    user = request.user

    # Devolvemos una respuesta que renderiza la plantilla del perfil
    return render(request, 'users/profile.html', {
        'user': user,  # Pasamos el usuario a la plantilla
    })
