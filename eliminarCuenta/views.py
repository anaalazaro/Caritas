from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import transaction
from app.models import CustomUser

from django.contrib import messages

@login_required
def delete_account(request, user_id):
    usuario_actual = request.user
    if usuario_actual.roles != 'usuario':
        # Si el usuario no tiene el rol de usuario normal, redirigir a alguna otra página o mostrar un mensaje de error
        return HttpResponse("No tienes permiso para acceder a esta página")
    try:
        usuario = CustomUser.objects.get(pk=user_id)
        usuario.delete()
        messages.success(request, 'La cuenta se ha eliminado exitosamente')
    except CustomUser.DoesNotExist:
        messages.error(request, '¡No se pudo encontrar la cuenta especificada!')

    return redirect('inicio')
