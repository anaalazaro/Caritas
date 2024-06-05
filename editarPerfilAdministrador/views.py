from django.shortcuts import render, redirect,reverse
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import UsuarioIntercambiadorForm
from app.models import CustomUser
from django.contrib import messages


def es_admin(user):
    return user.is_superuser

@login_required
@user_passes_test(es_admin)
def editar_perfil(request, usuario_id):
    usuario = CustomUser.objects.get(pk=usuario_id)
    if request.method == 'POST':
        form = UsuarioIntercambiadorForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            messages.success(request, 'Los cambios han sido guardados con éxito.')
            # url = reverse('editarPerfilAdmin', kwargs={'usuario_id': usuario_id})
            return redirect('inicio')
    else:
        form = UsuarioIntercambiadorForm(instance=usuario)
    return render(request, 'editarPerfil.html', {'form': form, 'user': usuario})