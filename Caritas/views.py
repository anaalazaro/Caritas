from django.contrib import messages
from django.shortcuts import render
from app.models import CustomUser
from cargarArticulo.models import Articulo
def hello(request):
    return render(request, 'inicio.html')

def mostrar(request):
    user=request.user
    sugeridos= Articulo.objects.filter(aprobado=True).exclude(usuario=request.user)
    return render (request, 'menuPrincipal.html', {'user': user, 'articulos':sugeridos })

def mostrarArticulosOrdenados(request):
   ordenados= Articulo.objects.filter(aprobado=True).exclude(usuario=request.user).order_by('Titulo')
   return render(request, 'menuPrincipal.html', {'user': request.user, 'articulos': ordenados})



def mostrarPorCategoria(request):
    if 'categoria' in request.GET:
        categoria_seleccionada = request.GET['categoria']
        articulos_filtrados = Articulo.objects.filter(aprobado=True, Categoria=categoria_seleccionada).exclude(usuario=request.user)
        if articulos_filtrados.exists():
            # Si hay artículos para la categoría seleccionada, los mostramos
            return render(request, 'menuPrincipal.html', {'user': request.user, 'articulos': articulos_filtrados})
        else:
            # Si no hay artículos para la categoría seleccionada, enviamos un mensaje
            messages.info(request, 'No hay artículos para la categoría seleccionada.')
            return render(request, 'menuPrincipal.html', {'user': request.user})
    else:
        # Si no se ha seleccionado ninguna categoría, puedes manejarlo de acuerdo a tu lógica
        pass
