from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .forms import ChangePasswordForm
from django.contrib import messages
from app.forms import CustomUser
import random
import string

def generate_random_password():
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(10))

def send_temp_password_email(user, temp_password):
    send_mail(
        'Tu nueva contraseña temporal',
        f'Tu nueva contraseña temporal es: {temp_password}',
        'from@example.com',
        [user.email],
        fail_silently=False,
    )

def change_password_request(request):
    if request.user.is_authenticated:
        # Si el usuario ya está autenticado, cerrar la sesión antes de proceder
        logout(request)

    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            try:
                user = CustomUser.objects.get(email=email)
                current_password = user.password
                # Almacenar la contraseña actual en la sesión antes de generar la nueva contraseña temporal
                request.session['current_password'] = current_password
                    
                temp_password = 'temp'#generate_random_password()
                user.set_password(temp_password)
                user.passChange = True
                user.save()
                send_temp_password_email(user, temp_password)
                print(f"Su contraseña autogenerada es {temp_password}")
                print(f"La contraseña anterior era {current_password}")
                return redirect('change_desired_password')
            except CustomUser.DoesNotExist:
                messages.error(request, 'El correo electrónico no está asociado a ninguna cuenta.')
    else:
        # Clear messages
        storage = messages.get_messages(request)
        storage.used = True

        form = ChangePasswordForm()
    return render(request, 'change_password.html', {'form': form})

def change_password_confirm(request):
    return render(request, 'change_password_confirm.html')