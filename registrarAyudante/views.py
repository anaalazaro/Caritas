from django.shortcuts import render,redirect
from .forms import CustomUserCreationForm
from app.models import CustomUser
from crearFilial.models import Filial
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
# Create your views here.
def es_admin(user):
    return user.is_superuser

@login_required
@user_passes_test(es_admin)
def registro(request):
    filiales = Filial.objects.filter(ayudante__isnull=True)
    formulario = CustomUserCreationForm()
    if filiales:
        if request.method == 'POST':
            formulario = CustomUserCreationForm(request.POST)
            print(formulario.data)  # Imprime los datos enviados por el formulario
            print(formulario.errors)  # Imprime los ERRORES enviados por el formulario
            if formulario.is_valid():
                user = formulario.save()
                #Se asigna el ayudante registrado a la filial seleccionada.
                filial_id = request.POST.get('filial')
                filial = Filial.objects.get(pk=filial_id)
                filial.ayudante = user
                filial.save()

                messages.success(request, 'Se ha creado al usuario ayudante exitosamente.')
                return redirect('verAyudantes')
        return render(request, 'singup.html', {'form': formulario})
    else:
        messages.info(request, 'No se puede registrar un ayudante porque no hay filiales disponibles. Por favor, cree una filial desde el menú principal.')
        return render(request, 'singup.html')