from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from cargarArticulo.models import Articulo

def eliminar_articulo(request, articulo_id):
    articulo = get_object_or_404(Articulo, pk=articulo_id)
    if request.method == 'POST':
        articulo.delete()
        messages.success(request, 'Artículo eliminado exitosamente')  # Envía el mensaje de éxito
        return redirect('verArticulos')  # Reemplaza 'lista_articulos' con el nombre de tu URL de lista de artículos
    return render(request, 'eliminar_articulo.html', {'articulo': articulo})