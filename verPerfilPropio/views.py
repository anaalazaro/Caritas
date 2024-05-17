from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Intercambiador# Importa tu modelo personalizado, si es necesario


@login_required  # Asegura que solo usuarios autenticados puedan acceder
def view_profile(request):
    # Obtenemos el usuario autenticado
    user = request.user

    # Devolvemos una respuesta que renderiza la plantilla del perfil
    return render(request, 'users/profile.html', {
        'user': user,  # Pasamos el usuario a la plantilla
    })
