from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from app.models import CustomUser
from .forms import LoginForm

def mostrar(request):
    return render (request, 'menuPrincipal.html', {'user': CustomUser})


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
<<<<<<< HEAD
                return redirect('menuPrincipal')
=======
                return HttpResponse("Inició sesión exitosamente")
>>>>>>> 410bfbfffd61f5190e29bcfd9e265d8f64bd63b3

            # Escenario 2 y 3: Fallos por usuario inexistente o contraseña incorrecta
            else:
                # Intento de usuario inexistente
<<<<<<< HEAD
                if not CustomUser.objects.filter(dni=dni).exists() :
                    error_message = "El usuario no existe"
=======
                if not Intercambiador.objects.filter(dni=dni).exists():
                    error_message = "El usuario y/o la contraseña son incorrectos"
>>>>>>> 410bfbfffd61f5190e29bcfd9e265d8f64bd63b3
                else:
                    error_message = "El usuario y/o la contraseña son incorrectos"
                    
                return render(request, 'autenticacionIntercambiador/login.html', {'form': form, 'error_message': error_message})

    else:
        form = LoginForm()

    return render(request, 'autenticacionIntercambiador/login.html', {'form': form})
