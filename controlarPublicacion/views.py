
from django.shortcuts import render, redirect, get_object_or_404
from cargarArticulo.models import Articulo
from django.contrib import messages
from django.contrib.auth.decorators import login_required

#@login_required
def controlar_publicacion(request, articulo_id):
    articulo = get_object_or_404(Articulo, pk=articulo_id)
    return render(request, 'controlar_publicacion.html', {'articulo': articulo})

#@login_required
def aprobar_articulo(request, articulo_id):
    articulo = get_object_or_404(Articulo, pk=articulo_id)
    articulo.pendiente = False
    articulo.aprobado = True
    articulo.save()
    message= 'La publicación se ha aprobado con éxito.'
    pendientes= Articulo.objects.filter(pendiente=True)
    return render(request, 'mostrarArticulosPendientes.html', {'success_message': message, 'articulos_pendientes': pendientes } )

#@login_required
def desaprobar_articulo(request, articulo_id):
    articulo = get_object_or_404(Articulo, pk=articulo_id)
    articulo.pendiente = False
    articulo.save()
    message= 'La publicación se ha desaprobado con éxito.'
    return render(request, 'mostrarArticulosPendientes.html', {'success_message': message })
