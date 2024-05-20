from django.shortcuts import render
from cargarArticulo.models import Articulo 


def mostrar_articulos_pendientes(request):
    articulos_pendientes = Articulo.objects.filter(pendiente=True)
    return render(request, 'mostrarArticulosPendientes.html', {'articulos_pendientes': articulos_pendientes})
