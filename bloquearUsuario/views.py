from django.shortcuts import render,redirect, get_object_or_404
from app.models import CustomUser
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator



@login_required
#@method_decorator(EsAdminOAyudanteMixin, name='dispatch')
#def lista_usuarios(request):
    # Filtrar solo los usuarios que están pendientes de bloqueo
    #users = CustomUser.objects.filter(pendiente_de_bloqueo=True)
    #return render(request, 'administracion/lista_usuarios.html', {'users': users})
#@method_decorator(EsAdminOAyudanteMixin, name='dispatch')
def bloquear_usuario(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    user.is_blocked = True
    user.pendiente_de_bloqueo = False  # Actualizar el estado de pendiente de bloqueo
    user.save()
    return redirect('lista_usuarios')
@login_required
#@method_decorator(EsAdminOAyudanteMixin, name='dispatch')
def lista_usuarios(request):
    # Filtrar solo los usuarios que están pendientes de bloqueo
    users = CustomUser.objects.filter(pendiente_de_bloqueo=True)
    return render(request, 'administracion/lista_usuarios.html', {'users': users})
