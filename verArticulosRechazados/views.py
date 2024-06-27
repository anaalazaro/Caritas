from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from cargarArticulo.models import Articulo

@login_required
def mostrarArticulosRechazados(request):
    rechazados = Articulo.objects.filter(pendiente=False, aprobado=False, usuario=request.user)
    print(rechazados)
    return render(request, 'articulos_rechazados.html', {'rechazados':rechazados})