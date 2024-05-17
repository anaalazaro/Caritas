from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from app.models import CustomUser  # Importa tu modelo personalizado

@login_required  # Asegura que solo usuarios autenticados puedan acceder
def view_profile(request):
    # Obtiene el usuario autenticado
    user = request.user
    
    # Verifica si el usuario autenticado está asociado a un CustomUser
    if CustomUser.objects.filter(dni=user.username).exists():
        # Obtiene el objeto CustomUser asociado al usuario autenticado
        custom_user = CustomUser.objects.get(dni=user.username)
        # Ahora puedes acceder a los campos del objeto CustomUser
        # Por ejemplo:
        telefono = custom_user.telefono
        fecha_nacimiento = custom_user.fechaNacimiento
        dni = custom_user.dni
        # Luego, puedes pasar esta información a la plantilla
        return render(request, 'verPerfilPropio/profile.html', {
            'user': user,  # Pasamos el usuario autenticado
            'custom_user': custom_user,  # Pasamos el objeto CustomUser
            'telefono': telefono,
            'fecha_nacimiento': fecha_nacimiento,
            'dni': dni,
        })
    else:
        # El usuario autenticado no está asociado a un CustomUser
        # Aquí puedes manejar este caso según tus necesidades
        return render(request, 'verPerfilPropio/profile.html', {
            'user': user,  # Pasamos el usuario autenticado
            'custom_user': None,  # No hay objeto CustomUser asociado
        })
