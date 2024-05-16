from django.shortcuts import render, redirect, get_object_or_404
from cargarArticulo.models import Articulo

def controlar_publicacion(request, articulo_id):
    articulo = get_object_or_404(Articulo, pk=articulo_id)
    return render(request, 'controlar_publicacion.html', {'articulo': articulo})

def aprobar_articulo(request, articulo_id):
    articulo = get_object_or_404(Articulo, pk=articulo_id)
    articulo.pendiente = False
    articulo.save()
    return redirect('controlar_publicacion', articulo_id=articulo_id)

def desaprobar_articulo(request, articulo_id):
    articulo = get_object_or_404(Articulo, pk=articulo_id)
    articulo.pendiente = False
    articulo.save()
    return redirect('controlar_publicacion', articulo_id=articulo_id)
