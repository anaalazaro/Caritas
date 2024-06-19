from django.shortcuts import render
from Caritas.views import custom_user_passes_test
from cargarArticulo.models import Articulo 
from django.contrib.auth.decorators import login_required

def es_ayudante(user):
    return user.roles == 'ayudante'

@login_required
@custom_user_passes_test(es_ayudante, message="No está habilitado para acceder a esta página.")
def mostrar_articulos_pendientes(request):
    articulos_pendientes = Articulo.objects.filter(pendiente=True)
    return render(request, 'mostrarArticulosPendientes.html', {'articulos_pendientes': articulos_pendientes})

@login_required
def mostrarArticulosPendientesPropios(request):
    pendientes= Articulo.objects.filter(pendiente=True, usuario=request.user)
    return render(request, 'misPublicacionesPendientes.html', {'pendientes':pendientes} )