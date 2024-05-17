from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .forms import DesiredPasswordChangeForm

@login_required(login_url='/login_otp') 
def change_desired_password(request):
    current_password = request.session.get('current_password')
    if not current_password:
        # Si la contraseña actual no está en la sesión, redirigir a la vista de cambio de contraseña temporal
        return redirect('change_password')

    if request.method == 'POST':
        form = DesiredPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            new_password = form.cleaned_data['new_password1']
            request.user.set_password(new_password)
            request.user.save()
            update_session_auth_hash(request, request.user)
            messages.success(request, '¡Tu contraseña ha sido cambiada correctamente!')
            # Eliminar la contraseña actual de la sesión después de cambiar la contraseña deseada
            del request.session['current_password']
            return redirect('main')  # Redirige a la página principal o donde desees
    else:
        form = DesiredPasswordChangeForm(user=request.user)
    return render(request, 'change_desired_password.html', {'form': form})

