from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import transaction
from app.models import CustomUser

from django.contrib import messages

def delete_account(request, user_id):
        usuario = CustomUser.objects.get(pk=user_id)
        usuario.delete()
        messages.success(request, 'La cuenta se ha eliminado exitosamente')
    