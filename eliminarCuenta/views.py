from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import transaction
from app.models import CustomUser

def delete_account(request, user_id):
    usuario = CustomUser.objects.get(pk=user_id)
    usuario_actual = request.user
    rol = usuario_actual.roles
    usuario.delete()
    messages.success(request, 'La cuenta se ha eliminado exitosamente')
    if 'admin' in rol:
        return redirect('verAyudantes')
    else:
        return redirect('inicio')
    
