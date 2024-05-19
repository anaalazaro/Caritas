from django.shortcuts import render
from app.models import CustomUser
from cargarArticulo.models import Articulo
def hello(request):
    return render(request, 'inicio.html')

def mostrar(request):
    user=request.user
    return render (request, 'menuPrincipal.html', {'user': user, 'articulos': Articulo.objects.filter(aprobado=False)})

def mostrarArticulosOrdenados(request):
   ordenados= Articulo.objects.all().order_by('Titulo')
   return render(request, 'menuPrincipal.html', {'user': CustomUser, 'articulos': ordenados})


from django.contrib import messages

def mostrarPorCategoria(request):
    if 'categoria' in request.GET:
        categoria_seleccionada = request.GET['categoria']
        articulos_filtrados = Articulo.objects.filter(categoria=categoria_seleccionada)
        if articulos_filtrados.exists():
            # Si hay artículos para la categoría seleccionada, los mostramos
            return render(request, 'menuPrincipal.html', {'user': CustomUser, 'articulos': articulos_filtrados})
        else:
            # Si no hay artículos para la categoría seleccionada, enviamos un mensaje
            messages.info(request, 'No hay artículos para la categoría seleccionada.')
            return render(request, 'menuPrincipal.html', {'user': CustomUser})
    else:
        # Si no se ha seleccionado ninguna categoría, puedes manejarlo de acuerdo a tu lógica
        pass
