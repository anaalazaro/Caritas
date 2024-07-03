from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import render
from solicitarIntercambio.models import Intercambio
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
from solicitarIntercambio.models import Intercambio
from django.utils import timezone
from datetime import datetime
from crearFilial.models import Filial, Turno
from django.core.mail import send_mail
from .formsEfectuar import OpcionesCodigos
from django.db.models import Q

def hello(request):
  #  if request.user.is_authenticated:
   #     if request.user.roles == 'usuario':
    #        user=request.user
     #       sugeridos= Articulo.objects.filter(aprobado=True).exclude(usuario=request.user)
      #      return render (request, 'menuPrincipal.html', {'user': user, 'articulos':sugeridos })
       # elif request.user.roles == 'ayudante':
        #    return redirect('inicioAyudante')
        #else:
         #   return redirect('inicioAdmin')
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
    borrados= CustomUser.objects.filter(borrado=True)
    for borrado in borrados:
        print("borrado",borrado.username)
    sugeridos= Articulo.objects.filter(aprobado=True, borrado=False, intercambiado=False).exclude((Q(usuario__in=borrados)) |(Q(usuario=request.user)))
    print(sugeridos)
    return render (request, 'menuPrincipal.html', {'user': user, 'articulos':sugeridos })

@login_required
def mostrarArticulosOrdenados(request):
    usuario_actual = request.user 
    if usuario_actual.roles != 'usuario':
       return HttpResponse("No tienes permiso para acceder a esta página")
    borrados= CustomUser.objects.filter(borrado=True)
    ordenados= Articulo.objects.filter(aprobado=True, borrado=False, intercambiado=False).exclude((Q(usuario__in=borrados)) |(Q(usuario=request.user))).order_by('Titulo')
    return render(request, 'menuPrincipal.html', {'user': request.user, 'articulos': ordenados})



@login_required
def mostrarPorCategoria(request):
    usuario_actual = request.user
    if usuario_actual.roles != 'usuario':
        # Si el usuario no tiene el rol de usuario normal, redirigir a alguna otra página o mostrar un mensaje de error
        return HttpResponse("No tienes permiso para acceder a esta página")
    if 'categoria' in request.GET:
        categoria_seleccionada = request.GET['categoria']
        borrados= CustomUser.objects.filter(borrado=True)
        articulos_filtrados = Articulo.objects.filter(aprobado=True, Categoria=categoria_seleccionada, borrado=False, intercambiado=False).exclude((Q(usuario__in=borrados)) |(Q(usuario=request.user)))
        if articulos_filtrados.exists():
            # Si hay artículos para la categoría seleccionada, los mostramos
            return render(request, 'menuPrincipal.html', {'user': request.user, 'articulos': articulos_filtrados})
        else:
            # Si no hay artículos para la categoría seleccionada, enviamos un mensaje
            messages.info(request, 'No hay artículos para la categoría seleccionada.')
            return render(request, 'menuPrincipal.html', {'user': request.user})
    else:
        articulos = Articulo.objects.filter(aprobado=True, borrado=False, intercambiado=False).exclude((Q(usuario__in=borrados)) |(Q(usuario=request.user)))
        # Si no se ha seleccionado ninguna categoría, puedes manejarlo de acuerdo a tu lógica
        return render(request, 'menuPrincipal.html', {'user': request.user, 'articulos': articulos})
    
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
    ahora = timezone.now()
    ahoraFalso = datetime(2024, 7, 6)
    # Formatear la fecha y hora en el formato de un campo DateTimeField
    formato_fecha = ahoraFalso.strftime('%Y-%m-%d')
    ayudanteActual= request.user
    filial_ayudante= Filial.objects.get(ayudante= ayudanteActual)
    #turnos de hoy para la filial_ayudante
    turnos_hoy= Turno.objects.filter(fecha= formato_fecha,filial= filial_ayudante)
    intercambios = Intercambio.objects.filter(turno__in=turnos_hoy, filial=filial_ayudante,estado= 'Aprobado')
    cantidad_intercambios_hoy= intercambios.count()
    return render(request, 'inicioAyudante.html', {'cantidad_intercambios':cantidad_intercambios_hoy})

@login_required
def mostrarIntercambiosDelDia(request):
    ahora = timezone.now()
    ahoraFalso = datetime(2024, 7, 6)
    # Formatear la fecha y hora en el formato de un campo DateTimeField
    formato_fecha = ahoraFalso.strftime('%Y-%m-%d')
    ayudanteActual= request.user
    filial_ayudante= Filial.objects.get(ayudante= ayudanteActual)
    #turnos de hoy para la filial_ayudante
    turnos_hoy= Turno.objects.filter(fecha= formato_fecha,filial= filial_ayudante)
    intercambios = Intercambio.objects.filter(turno__in=turnos_hoy, filial=filial_ayudante,estado='Aprobado')
    return render(request, 'listadoIntercambiosHoy.html', {'intercambios': intercambios})

def promedio(numero1,numero2):
    suma = numero1 + numero2
    return suma / 2

@login_required
def efectuarIntercambio(request, codigo_intercambio):
    input_solicitante = False
    input_destinatario = False
    if request.method == 'POST':
        form = OpcionesCodigos(request.POST)
        if form.is_valid():
            seleccion = form.cleaned_data['seleccion']
            if seleccion == 'opcion1':
                input_solicitante = True
                input_destinatario = True
            elif seleccion == 'opcion2':
                input_solicitante = True
                input_destinatario = False
            elif seleccion == 'opcion3':
                input_destinatario = True
                input_solicitante = False
        intercambio= get_object_or_404(Intercambio,codigo_intercambio= codigo_intercambio)
        codigo_solicitante = request.POST.get('codigo_solicitante')
        codigo_destinatario = request.POST.get('codigo_destinatario')
        if  codigo_solicitante and codigo_destinatario:
            if codigo_solicitante == intercambio.codigo_intercambio_solicitante and codigo_destinatario == intercambio.codigo_intercambio_destinatario:    
                intercambio.estado= 'Efectuado'
                #se promedia el puntaje de cada user intercambiador
                intercambio.solicitante.puntaje +=0.5
                intercambio.destinatario.puntaje +=0.5
                intercambio.destinatario.save()
                intercambio.destinatario.save()
                intercambio.save()
                intercambio.articulo_ofrecido.intercambiado=True
                intercambio.articulo_solicitado.intercambiado=True
                intercambio.articulo_ofrecido.save()
                intercambio.articulo_solicitado.save()
                send_mail(
                    'Intercambio',
                    f'¡Se ha efectuado el intercambio con código {intercambio.codigo_intercambio} exitosamente! Si lo deseas, puedes calificar al usuario con el que has realizado el intercambio, dirígete a su perfil y deja tu reseña.',
                'ingecaritas@gmail.com',
                    [intercambio.destinatario.mail,intercambio.solicitante.mail],
                    fail_silently=False,
                )
                # send_mail(
                #     'Intercambio',
                #     f'¡Se ha efectuado el intercambio con código {intercambio.codigo_intercambio} exitosamente! Si lo deseas, puedes calificar al usuario con el que has realizado el intercambio, dirígete a su perfil y deja tu reseña.',
                # 'ingecaritas@gmail.com',
                #     [intercambio.solicitante.mail],
                #     fail_silently=False,
                # )
                messages.success(request, 'El intercambio se ha efectuado exitosamente.')               
                return redirect('listadoIntercambiosAyudante')
            else:
                messages.error(request, 'Código invalido. Alguno de los códigos ingresados no es válido.')
        elif codigo_solicitante and not codigo_destinatario:
            if codigo_solicitante == intercambio.codigo_intercambio_solicitante:
                intercambio.estado= 'No Efectuado'
                #se promedia el puntaje de cada user intercambiador
                intercambio.solicitante.puntaje +=0.5
                intercambio.destinatario.puntaje -= 0.5
                intercambio.solicitante.save()
                intercambio.destinatario.save()
                intercambio.save()
                send_mail(
                        'Intercambio',
                        f'¡No se ha efectuado el intercambio con código {intercambio.codigo_intercambio}!.',
                    'ingecaritas@gmail.com',
                        [intercambio.solicitante.mail,intercambio.destinatario.mail],
                        fail_silently=False,
                    )
                # send_mail(
                #         'Intercambio',
                #         f'¡Se ha efectuado el intercambio con código {intercambio.codigo_intercambio} exitosamente! Si lo deseas, puedes calificar al usuario con el que has realizado el intercambio, dirígete a su perfil y deja tu reseña.',
                #     'ingecaritas@gmail.com',
                #         [intercambio.destinatario.mail],
                #         fail_silently=False,
                #     )
                messages.success(request, 'El intercambio no se ha efectuado.')
                return redirect('listadoIntercambiosAyudante')
            else:
                messages.error(request, 'Código invalido. El código ingresado no es válido.')
        elif not codigo_solicitante and codigo_destinatario:
            if codigo_destinatario == intercambio.codigo_intercambio_destinatario:
                intercambio.estado= 'No Efectuado'
                #se promedia el puntaje de cada user intercambiador
                intercambio.solicitante.puntaje -= 0.5
                intercambio.destinatario.puntaje +=0.5
                intercambio.solicitante.save()
                intercambio.destinatario.save()
                print("Entró al destinatario", intercambio.solicitante.puntaje)
                intercambio.save()
                send_mail(
                        'Intercambio',
                        f'¡No se ha efectuado el intercambio con código {intercambio.codigo_intercambio}!',
                    'ingecaritas@gmail.com',
                        [intercambio.destinatario.mail,intercambio.solicitante.mail],
                        fail_silently=False,
                    )
                # send_mail(
                #         'Intercambio',
                #         f'¡No se ha efectuado el intercambio con código {intercambio.codigo_intercambio}!',
                #     'ingecaritas@gmail.com',
                #         [intercambio.destinatario.mail],
                #         fail_silently=False,
                #     )
                messages.success(request, 'El intercambio no se ha efectuado.')
                return redirect('listadoIntercambiosAyudante')
            else:
                messages.error(request, 'Código invalido. El código ingresado no es válido.')
            
    else:
        form = OpcionesCodigos()
    return render(request, 'efectuarIntercambio.html', {'codigo_intercambio':codigo_intercambio,'form':form,'input_solicitante':input_solicitante,'input_destinatario':input_destinatario})            

def marcar_leida(request, notification_id):
    notification = get_object_or_404(Notification, pk=notification_id)
    notification.is_read = True
    notification.save()
    return JsonResponse({'status': 'success'})

@login_required
@custom_user_passes_test(es_admin, message="No está habilitado para acceder a esta página.")
def eliminarArticulo(request, articulo_id):
     articulo= Articulo.objects.get(pk= articulo_id)
     articulo.borrado=True
     articulo.save()
     HttpResponse("Se eliminó con éxito")

@login_required
@custom_user_passes_test(es_admin, message="No está habilitado para acceder a esta página.")
def mostrarArticulosAEliminar(request):
    eliminar= Articulo.objects.filter(aprobado=False, pendiente=False, borrado=False)
    return render(request, 'listarEliminados.html', {'articulos': eliminar})
                  
@login_required
def mostrarSolictudesIntercambios(request):
    intercambios= Intercambio.objects.filter(destinatario=request.user,estado='Pendiente')
    print(intercambios)
    return render(request, 'listaIntercambiosSolicitantes.html', {'intercambios': intercambios})

@login_required
def mostrarIntercambiosPropuestos(request):
    intercambios= Intercambio.objects.filter(solicitante=request.user)
    print(intercambios)
    return render(request, 'listadoIntercambiosPropuestos.html', {'intercambios': intercambios})

@login_required
def mostrarIntercambios(request):
    intercambios = Intercambio.objects.filter(
        Q(destinatario=request.user) | Q(solicitante=request.user)
        ).exclude(
        estado='Pendiente'
        )
    print(intercambios)
    return render(request, 'listadoIntercambios.html', {'intercambios': intercambios})

@login_required
def mostrarIntercambiosAyudante(request):
    
    ayudanteActual= request.user
    filial_ayudante= Filial.objects.get(ayudante= ayudanteActual)
    estados_a_excluir = ['Pendiente', 'Aprobado', 'Rechazado']
    intercambios = Intercambio.objects.filter(filial=filial_ayudante).exclude(estado__in=estados_a_excluir)
    print(intercambios)
    return render(request, 'listadoIntercambiosAyudante.html', {'intercambios': intercambios})

def confirmarBloqueo(request, user_id):
    usuario= CustomUser.objects.get(pk= user_id)
    return render(request, 'confirmarBloqueo.html', {'usuario': usuario})


@login_required
def ver_historial_intercambios(request):
    # Asegúrate de que el usuario sea administrador
    if not request.user.is_superuser:
        return HttpResponseForbidden("No tienes permiso para acceder a esta página")
    intercambios = Intercambio.objects.all()

    # Verificar si hay intercambios
    if not intercambios.exists():
        mensaje = "No se encontraron solicitudes de intercambios"
        return render(request, 'historial_intercambios.html', {'mensaje': mensaje})

    return render(request, 'historial_intercambios.html', {'intercambios': intercambios}) 
