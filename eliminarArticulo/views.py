from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from cargarArticulo.models import Articulo
from app.forms import CustomUser

def eliminar_articulo(request, articulo_id):
    articulo = get_object_or_404(Articulo, pk=articulo_id)
    if request.method == 'POST':
        articulo.delete()
        messages.success(request, 'Artículo eliminado exitosamente')  # Envía el mensaje de éxito
        if request.user.roles == 'admin':
           return redirect('listarAEliminar')  # Reemplaza 'lista_articulos' con el nombre de tu URL de lista de artículos
        else:
           return redirect('verArticulos') 
    return render(request, 'eliminar_articulo.html', {'articulo': articulo})