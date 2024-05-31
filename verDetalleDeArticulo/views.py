from django.shortcuts import render, get_object_or_404
from cargarArticulo.models import Articulo
from django.contrib.auth.decorators import login_required

@login_required
def mostrarDetalle(request, articulo_id):
    articulo = get_object_or_404(Articulo, pk=articulo_id)
    return render(request, 'detalleDeArticulo.html', {'articulo': articulo})



