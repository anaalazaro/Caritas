from django.shortcuts import render
from app.models  import CustomUser
from crearFilial.models import Filial
from django.contrib.auth.decorators import login_required, user_passes_test

def es_admin(user):
    return user.is_superuser

@login_required
@user_passes_test(es_admin)

def ver_ayudantes(request):
    # Filtra los usuarios por el rol de "ayudante"
    ayudantes = CustomUser.objects.filter(roles='ayudante', borrado=False)
    ayudantesF = []
    for ayudante in ayudantes:
        filial = ayudante.filial_set.first()  # Obtiene la filial asociada al ayudante (si existe)
        ayudantesF.append({'ayudante': ayudante, 'filial': filial})
    return render(request, 'verAyudantes.html', {'ayudantes': ayudantesF})

def confirmar_eliminar_ayudante(request, user_id):
    user = CustomUser.objects.get(id=user_id)
    return render(request, 'confirmar_eliminar_ayudante.html', {'user': user})