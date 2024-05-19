from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ArticuloForm
from .models import Articulo

@login_required
def cargar_articulo(request):
    if request.method == 'POST':
        form = ArticuloForm(request.POST, request.FILES, usuario=request.user)
        if form.is_valid():
            form.save()
            return redirect('nombre_de_la_vista')
    else:
        form = ArticuloForm(usuario=request.user)
    return render(request, 'cargarArticulo.html', {'form': form})
