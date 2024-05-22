from functools import wraps
from django.contrib import messages
from django.http import HttpResponseForbidden
from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from app.models import CustomUser
from cargarArticulo.models import Articulo
from django.contrib.auth.decorators import login_required, user_passes_test
from notificaciones.models import Notification
from django.http import JsonResponse


def hello(request):
    if request.user.is_authenticated:
        if request.user.roles == 'usuario':
            user=request.user
            sugeridos= Articulo.objects.filter(aprobado=True).exclude(usuario=request.user)
            return render (request, 'menuPrincipal.html', {'user': user, 'articulos':sugeridos })
        elif request.user.roles == 'ayudante':
            return redirect('inicioAyudante')
        else:
            return redirect('inicioAdmin')
    return render(request, 'inicio.html')

@login_required
def confirmar_eliminar_cuenta(request):
    return render(request, 'confirmar_eliminar_cuenta.html')
@login_required
def mostrar(request):
    usuario_actual = request.user
    if usuario_actual.roles != 'usuario':
        # Si el usuario no tiene el rol de usuario normal, redirigir a alguna otra página o mostrar un mensaje de error
        return HttpResponse("No tienes permiso para acceder a esta página")
    user=request.user
    sugeridos= Articulo.objects.filter(aprobado=True).exclude(usuario=request.user)
    print(sugeridos)
    return render (request, 'menuPrincipal.html', {'user': user, 'articulos':sugeridos })

@login_required
def mostrarArticulosOrdenados(request):
    usuario_actual = request.user
    if usuario_actual.roles != 'usuario':
       return HttpResponse("No tienes permiso para acceder a esta página")
    ordenados= Articulo.objects.filter(aprobado=True).exclude(usuario=request.user).order_by('Titulo')
    return render(request, 'menuPrincipal.html', {'user': request.user, 'articulos': ordenados})


@login_required
def mostrarPorCategoria(request):
    usuario_actual = request.user
    if usuario_actual.roles != 'usuario':
        # Si el usuario no tiene el rol de usuario normal, redirigir a alguna otra página o mostrar un mensaje de error
        return HttpResponse("No tienes permiso para acceder a esta página")
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
def es_admin(user):
    return user.is_superuser

def es_ayudante(user):
    return user.roles == 'ayudante'

def custom_user_passes_test(test_func, message):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if test_func(request.user):
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponseForbidden(message)
        return _wrapped_view
    return decorator

@login_required
@custom_user_passes_test(es_admin, message="No está habilitado para acceder a esta página.")
def inicioAdmin(request):
    return render (request, 'inicioAdmin.html')

@login_required
@custom_user_passes_test(es_ayudante, message="No está habilitado para acceder a esta página.")
def inicioAyudante(request):
    return render(request, 'inicioAyudante.html')


def marcar_leida(request, notification_id):
    notification = get_object_or_404(Notification, pk=notification_id)
    notification.is_read = True
    notification.save()
    return JsonResponse({'status': 'success'})
