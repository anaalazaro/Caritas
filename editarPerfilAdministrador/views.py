from django.shortcuts import render, redirect,reverse
from .forms import UsuarioIntercambiadorForm
from app.models import CustomUser

def editar_perfil(request, usuario_id):
    usuario = CustomUser.objects.get(pk=usuario_id)
    if request.method == 'POST':
        form = UsuarioIntercambiadorForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            url = reverse('editarPerfilAdmin', kwargs={'usuario_id': usuario_id})
            return redirect(url)
    else:
        form = UsuarioIntercambiadorForm(instance=usuario)
    return render(request, 'editarPerfil.html', {'form': form})