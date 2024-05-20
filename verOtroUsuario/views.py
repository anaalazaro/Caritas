from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from app.models import CustomUser
from cargarArticulo.models import Articulo

@login_required
def view_other_profile(request, user_id):
    other_user = get_object_or_404(CustomUser, id=user_id)
    return render(request, 'verUsuario.html', {'user_profile': other_user})

def verProductos(request, user_profile_id):
    articulos= Articulo.objects.filter(usuario_id=user_profile_id, aprobado=True)
    return render(request, 'verArticulos.html', {'articulos': articulos})