from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ArticuloForm
from django.core.mail import send_mail
from django.contrib.auth.models import User
from app.models import CustomUser
from notificaciones.models import Notification

from django.shortcuts import redirect, render
from django.contrib import messages
from django.urls import reverse


@login_required
def cargar_articulo(request):
    usuario_actual = request.user
    if usuario_actual.roles != 'usuario':
        # Si el usuario no tiene el rol de usuario normal, redirigir a alguna otra página o mostrar un mensaje de error
        return HttpResponse("No tienes permiso para acceder a esta página")
    if request.method == 'POST':
        form = ArticuloForm(request.POST, request.FILES)
        if form.is_valid():
            articulo = form.save(commit=False)
            articulo.usuario = request.user
            articulo.pendiente = True  # Establece el estado del artículo como pendiente
            articulo.save()
            messages.success(request, 'La publicación del artículo ha quedado pendiente a la aprobación del ayudante.')
            ayudante = CustomUser.objects.filter(roles='ayudante',borrado=False).first()
            Notification.objects.create(
            sender=request.user,
            user=ayudante,
            message=f'Hola "{ayudante.username}" hay un nuevo artículo pendiente de revisión.',
            )
            return redirect(reverse('menuPrincipal') + '?mensaje=El+artículo+quedó+pendiente+de+aprobación+por+el+ayudante')
    else:
        form = ArticuloForm()
    return render(request, 'cargarArticulo.html', {'form': form})