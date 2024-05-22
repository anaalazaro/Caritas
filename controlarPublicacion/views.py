
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from Caritas.views import custom_user_passes_test
from app.models import CustomUser
from cargarArticulo.models import Articulo
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from notificaciones.models import Notification

def es_ayudante(user):
    return user.roles == 'ayudante'

@login_required
@custom_user_passes_test(es_ayudante, message="No está habilitado para acceder a esta página.")
def controlar_publicacion(request, articulo_id):
    articulo = get_object_or_404(Articulo, pk=articulo_id)
    return render(request, 'controlar_publicacion.html', {'articulo': articulo})

@login_required
@custom_user_passes_test(es_ayudante, message="No está habilitado para acceder a esta página.")
def aprobar_articulo(request, articulo_id):
    articulo = get_object_or_404(Articulo, pk=articulo_id)
    articulo.pendiente = False
    articulo.aprobado = True
    articulo.save()
    message= 'La publicación se ha aprobado con éxito.'
    pendientes= Articulo.objects.filter(pendiente=True)
    return render(request, 'mostrarArticulosPendientes.html', {'success_message': message, 'articulos_pendientes': pendientes } )

@login_required
@custom_user_passes_test(es_ayudante, message="No está habilitado para acceder a esta página.")
def desaprobar_articulo(request, articulo_id):
    articulo = get_object_or_404(Articulo, pk=articulo_id)
    articulo.pendiente = False
    articulo.save()
    administrador = CustomUser.objects.get(roles='admin')
    Notification.objects.create(
            sender=request.user,
            user=administrador,
            message=f'Hola "{administrador.username}" hay un nuevo artículo a eliminar',
            )
    message= 'La publicación se ha desaprobado con éxito.'
    return render(request, 'mostrarArticulosPendientes.html', {'success_message': message })
