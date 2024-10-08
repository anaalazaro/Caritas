from django.shortcuts import render, get_object_or_404, redirect
from .models import Intercambio
from cargarArticulo.models import Articulo
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from notificaciones.models import Notification
from django.utils.crypto import get_random_string
from django.core.mail import send_mail

@login_required
def solicitar_intercambio(request, articulo_id):
    articulo_solicitado = get_object_or_404(Articulo, id=articulo_id)
    solicitante = request.user
    destinatario = articulo_solicitado.usuario

    
    if solicitante.puntaje < 2:
        messages.error(request, 'No tienes suficiente calificación para solicitar un intercambio.')
        return redirect('menuPrincipal')

    if solicitante.solicitudes_enviadas.filter(estado='Pendiente').count() >= 5:
        messages.error(request, 'Tienes demasiadas solicitudes pendientes.No puedes solicitar otro intercambio.')
        return redirect('menuPrincipal')

    if request.method == 'POST':
        articulo_ofrecido_id = request.POST.get('articulo_ofrecido')
        articulo_ofrecido = get_object_or_404(Articulo, id=articulo_ofrecido_id)

        if articulo_solicitado.Categoria != articulo_ofrecido.Categoria:
            messages.error(request, 'Los artículos deben ser de la misma Categoria.')
            return redirect('solicitar_intercambio', articulo_id=articulo_id)
        
        if solicitante.solicitudes_enviadas.filter(estado='Pendiente',articulo_ofrecido=articulo_ofrecido):
            messages.error(request, f'Ya tienes una solicitud de intercambio para el articulo que deseas ofrecer.')
            return redirect('solicitar_intercambio', articulo_id=articulo_id)

        cod_intercambio = get_random_string(15)
        solicitud = Intercambio.objects.create(
            solicitante=solicitante,
            destinatario=destinatario,
            articulo_solicitado=articulo_solicitado,
            articulo_ofrecido=articulo_ofrecido,
            codigo_intercambio = cod_intercambio
        )

        Notification.objects.create(
            sender=solicitante,
            user=destinatario,
            message=f'Hola "{destinatario.nombre}" tienes una nueva solicitud de intercambio pendiente.',
            )
        send_mail(
                'Solicitud de intercambio',
                f'¡Hola {destinatario.nombre}, tienes una nueva solicitud de intercambio pendiente',
                'ingecaritas@gmail.com',
                [destinatario.mail],
                fail_silently=False,
            )
        messages.success(request, 'Solicitud de intercambio realizada con éxito.')
        return redirect('menuPrincipal')

    articulos_propios = Articulo.objects.filter(usuario=solicitante,aprobado=True)
    return render(request, 'solicitarIntercambio.html', {'articulo_solicitado': articulo_solicitado, 'articulos_propios': articulos_propios})
