
from django.shortcuts import render, redirect, get_object_or_404
from cargarArticulo.models import Articulo
from django.contrib import messages

def controlar_publicacion(request, articulo_id):
    articulo = get_object_or_404(Articulo, pk=articulo_id)
    return render(request, 'controlar_publicacion.html', {'articulo': articulo})

def aprobar_articulo(request, articulo_id):
    articulo = get_object_or_404(Articulo, pk=articulo_id)
    articulo.pendiente = False
    articulo.aprobado = True
    articulo.save()
    messages.success(request, 'La publicación se ha aprobado con éxito.')
    return redirect('controlar_articulo', articulo_id=articulo_id)

def desaprobar_articulo(request, articulo_id):
    articulo = get_object_or_404(Articulo, pk=articulo_id)
    articulo.pendiente = False
    articulo.save()
    messages.success(request, 'La publicación se ha desaprobado con éxito.')
    return redirect('controlar_articulo', articulo_id=articulo_id)
