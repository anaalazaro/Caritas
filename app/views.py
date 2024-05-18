
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from autenticacionIntercambiador.models import Intercambiador
from autenticacionIntercambiador.models import LoginForm
from .forms import CustomUserCreationForm





def registro(request):
    data = {'form': CustomUserCreationForm()}

    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)

        if user_creation_form.is_valid():
            telefono = user_creation_form.cleaned_data['telefono']
            # Verificar si el número de teléfono es de La Plata y Argentina
            if not telefono.startswith('221'):
                # Si el número de teléfono no es válido, añadir un mensaje de error al formulario
                user_creation_form.add_error('telefono', 'El teléfono debe corresponder a La Plata')
            else:
                # Si el formulario es válido, guardar el usuario y autenticarlo
                user = user_creation_form.save()
                username = user_creation_form.cleaned_data['dni']
                password = user_creation_form.cleaned_data['password1']
                user = authenticate(request, username=username, password=password)
              #  login(request, user)
                return redirect('inicio')  # Redirigir al usuario a la página de inicio

        # Si el formulario no es válido, actualizar los datos con el formulario y sus errores
        data['form'] = user_creation_form

    return render(request, 'registro/registroUsuario.html', data)
