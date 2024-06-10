from django.shortcuts import redirect, render
from app.models import CustomUser

def verUsuariosParaBloquear(request):
    usuarios_a_bloquear = CustomUser.objects.filter(pendiente_bloqueo=True)
    return render(request, 'listadoABloquear.html', {'usuarios_a_bloquear': usuarios_a_bloquear})

def verUsuariosBloqueados(request):
    usuarios_bloqueados = CustomUser.objects.filter(is_blocked=True)
    return render(request, 'listadoBloqueados.html', {'usuarios_bloq': usuarios_bloqueados})