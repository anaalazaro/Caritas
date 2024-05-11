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
