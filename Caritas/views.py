from django.shortcuts import render
from app.models import CustomUser
from cargarArticulo.models import Articulo
def hello(request):
    return render(request, 'inicio.html')

def mostrar(request):
    return render (request, 'menuPrincipal.html', {'user': CustomUser, 'articulos': Articulo.objects.filter(aprobado=False)})

def mostrarArticulosOrdenados(request):
   ordenados= Articulo.objects.all().order_by('Titulo')
   return render(request, 'menuPrincipal.html', {'user': CustomUser, 'articulos': ordenados})



