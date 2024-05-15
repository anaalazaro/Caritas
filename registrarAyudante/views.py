from django.shortcuts import render,redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login

# Create your views here.
# def home(request):
#     return render(request,'inicio.html')

def registro(request):
    if request.method == 'POST':
        formulario = CustomUserCreationForm(request.POST)
        print(formulario.data)  # Imprime los datos enviados por el formulario
        print(formulario.errors)  # Imprime los ERRORES enviados por el formulario
        if formulario.is_valid():
            formulario.save()
            username = formulario.cleaned_data['dni']
            password = formulario.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('registro')
    else:
         formulario = CustomUserCreationForm()
    return render(request, 'singup.html', {'form': formulario})