from django.shortcuts import render
from app.models import CustomUser
from django.contrib.auth.decorators import login_required, user_passes_test

def hello(request):
    return render(request, 'inicio.html')

def mostrar(request):
    return render (request, 'menuPrincipal.html', {'user': CustomUser})

def es_admin(user):
    return user.is_superuser

@login_required
@user_passes_test(es_admin)
def inicioAdmin(request):
    return render (request, 'inicioAdmin.html')

