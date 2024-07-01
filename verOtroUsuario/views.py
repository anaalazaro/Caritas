from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from app.models import CustomUser
from cargarArticulo.models import Articulo

@login_required
def view_other_profile(request, user_id):
    usuario_actual = request.user
    if usuario_actual.roles != 'usuario':
        # Si el usuario no tiene el rol de usuario normal, redirigir a alguna otra página o mostrar un mensaje de error
        return HttpResponse("No tienes permiso para acceder a esta página")
    other_user = get_object_or_404(CustomUser, id=user_id)
    return render(request, 'verUsuario.html', {'user_profile': other_user})

@login_required
def verProductos(request, user_profile_id):
    usuario_actual = request.user
    if usuario_actual.roles != 'usuario':
        # Si el usuario no tiene el rol de usuario normal, redirigir a alguna otra página o mostrar un mensaje de error
        return HttpResponse("No tienes permiso para acceder a esta página")
    articulos= Articulo.objects.filter(usuario_id=user_profile_id, aprobado=True, borrado=False)
    return render(request, 'verArticulos.html', {'articulos': articulos})