from django.shortcuts import render,redirect
from .forms import CustomUserCreationForm
from .models import Filial, CustomUser
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
# Create your views here.
def es_admin(user):
    return user.is_superuser

@login_required
@user_passes_test(es_admin)
def registro(request):
    if request.method == 'POST':
        formulario = CustomUserCreationForm(request.POST)
        print(formulario.data)  # Imprime los datos enviados por el formulario
        print(formulario.errors)  # Imprime los ERRORES enviados por el formulario
        if formulario.is_valid():
            user = formulario.save(commit=False)
            # Verifica si se seleccionó una filial en el formulario
            filial_id = request.POST.get('filial')
            if filial_id:
                # Asigna la filial al usuario
                filial = Filial.objects.get(pk=filial_id)
                user.filial = filial
                print(CustomUser.objects.filter(filial=filial).exists())
                if CustomUser.objects.filter(filial=filial).exists():
                    messages.error(request, 'Esta filial ya tiene un ayudante asignado.')
                    return redirect('registro')
            user.save()
            messages.success(request, 'Se ha creado al usuario ayudante exitosamente.')
            # username = formulario.cleaned_data['dni']
            # password = formulario.cleaned_data['password1']
            # # user = authenticate(request, username=username, password=password)
            # # login(request, user)
            return redirect('verAyudantes')
    else:
         formulario = CustomUserCreationForm()
    return render(request, 'singup.html', {'form': formulario})