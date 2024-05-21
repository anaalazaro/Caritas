from django.shortcuts import render
from cargarArticulo.models import Articulo 
from django.contrib.auth.decorators import login_required


#@login_required
def mostrar_articulos_pendientes(request):
    articulos_pendientes = Articulo.objects.filter(pendiente=True)
    return render(request, 'mostrarArticulosPendientes.html', {'articulos_pendientes': articulos_pendientes})
