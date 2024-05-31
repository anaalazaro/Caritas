from django.shortcuts import render,HttpResponse
from cargarArticulo.models import Articulo
from django.contrib.auth.decorators import login_required

@login_required
def ver_articulos(request):
    usuario_actual = request.user
    if usuario_actual.roles != 'usuario':
        # Si el usuario no tiene el rol de usuario normal, redirigir a alguna otra página o mostrar un mensaje de error
        return HttpResponse("No tienes permiso para acceder a esta página")
    articulos = Articulo.objects.filter(usuario=usuario_actual,aprobado=True)

    return render(request, 'verArticulosPropios.html', {'articulos': articulos})