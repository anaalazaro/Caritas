from django.shortcuts import render
from app.models  import CustomUser
from django.contrib.auth.decorators import login_required, user_passes_test

def es_admin(user):
    return user.is_superuser

@login_required
@user_passes_test(es_admin)

def ver_intercambiadores(request):
    # Filtra los usuarios por el rol de "ayudante"
    usuarios = CustomUser.objects.filter(roles='usuario')
    return render(request, 'verIntercambiadores.html', {'usuarios': usuarios})