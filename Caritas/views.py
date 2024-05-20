from django.contrib import messages
from django.shortcuts import render
from app.models import CustomUser
<<<<<<< HEAD
from cargarArticulo.models import Articulo
=======
from django.contrib.auth.decorators import login_required, user_passes_test

>>>>>>> ana
def hello(request):
    return render(request, 'inicio.html')

def mostrar(request):
    user=request.user
    sugeridos= Articulo.objects.filter(aprobado=True).exclude(usuario=request.user)
    return render (request, 'menuPrincipal.html', {'user': user, 'articulos':sugeridos })

<<<<<<< HEAD
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
=======
def es_admin(user):
    return user.is_superuser

@login_required
@user_passes_test(es_admin)
def inicioAdmin(request):
    return render (request, 'inicioAdmin.html')

>>>>>>> ana
