from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import transaction
from app.models import CustomUser

def delete_account(request, user_id):
    usuario = CustomUser.objects.get(pk=user_id)
    usuario_actual = request.user
    usuario.delete()
    messages.success(request, 'La cuenta se ha eliminado exitosamente')
    if 'admin' in usuario_actual.roles:
        return redirect('verAyudantes')
    else:
        return redirect('inicio')
    
