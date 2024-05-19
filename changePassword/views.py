from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from app.forms import CustomUser
from .forms import DesiredPasswordChangeForm

@login_required(login_url='login') 
def change_desired_password(request):
    current_password = request.session.get('current_password')
    print(current_password)
    if not current_password:
        # Si la contraseña actual no está en la sesión, redirigir a la vista de cambio de contraseña temporal
        return redirect('change_password')

    if request.method == 'POST':
        form = DesiredPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            new_password = form.cleaned_data['new_password1']
            if check_password(new_password, current_password):
                messages.error(request, 'La nueva contraseña no puede ser idéntica a la contraseña anterior.')
            else:
                request.user.set_password(new_password)
                request.user.passChange = False
                request.user.save()
                update_session_auth_hash(request, request.user)
                messages.success(request, '¡Tu contraseña ha sido cambiada correctamente!')
                # Eliminar la contraseña actual de la sesión después de cambiar la contraseña deseada
                del request.session['current_password']
                custom_user = CustomUser.objects.get(pk=request.user.pk)
                return mostrar(request, custom_user=custom_user)
    else:
        form = DesiredPasswordChangeForm(user=request.user)
    return render(request, 'change_desired_password.html', {'form': form})

def mostrar(request, custom_user):
    return render (request, 'cambio_exitoso.html', {'user': custom_user})