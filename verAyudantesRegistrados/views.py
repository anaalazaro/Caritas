from django.shortcuts import render
from registrarAyudante.models  import CustomUser
from django.contrib.auth.decorators import login_required, user_passes_test

def es_admin(user):
    return user.is_superuser

@login_required
@user_passes_test(es_admin)

def ver_ayudantes(request):
    # Filtra los usuarios por el rol de "ayudante"
    ayudantes = CustomUser.objects.filter(roles='ayudante')
    return render(request, 'verAyudantes.html', {'ayudantes': ayudantes})