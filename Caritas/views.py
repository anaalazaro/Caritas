from django.shortcuts import render
from app.models import CustomUser
def hello(request):
    return render(request, 'inicio.html')

def mostrar(request):
    return render (request, 'menuPrincipal.html', {'user': CustomUser})

