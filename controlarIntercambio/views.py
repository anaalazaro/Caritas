from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from solicitarIntercambio.models import Intercambio
from django.core.mail import send_mail
from crearFilial.models import Filial,Turno
from .forms import RechazarIntercambioForm
from django.utils.crypto import get_random_string
from django.contrib.auth.decorators import login_required
from datetime import date,timedelta
import folium

@login_required
def controlar_intercambio(request, intercambio_id):
    filiales = Filial.objects.filter(ayudante__isnull=False)
    filial_seleccionada = None
    turnos_disponibles = None
    intercambio = get_object_or_404(Intercambio, id=intercambio_id)
    un_mes_despues = date.today() + timedelta(days=30)

    if 'filial_id' in request.GET:
        filial_id = request.GET['filial_id']
        filial_seleccionada = get_object_or_404(Filial, id=filial_id)
        turnos_disponibles = Turno.objects.filter(filial=filial_seleccionada, turnos_disponibles__gt=0, fecha__gte=date.today(), fecha__lte=un_mes_despues)

    # Crea el mapa con Folium
    mapa = folium.Map(location=[-34.9205, -57.9536], zoom_start=13)

    # Añade un marcador para cada filial, marcando en rojo el de la filial seleccionada
    for filial in filiales:
        if filial.latitud and filial.longitud:
            if filial==filial_seleccionada:
                folium.Marker([filial.latitud, filial.longitud], icon=folium.Icon(prefix='fa', icon='location-mark', color='green'), popup=filial.nombre).add_to(mapa)
            else:
                folium.Marker([filial.latitud, filial.longitud], popup=filial.nombre).add_to(mapa)

    context = {
        'filiales': filiales,
        'filial_seleccionada': filial_seleccionada,
        'turnos_disponibles': turnos_disponibles,
        'intercambio': intercambio,
        'mapa': mapa._repr_html_(),  # Convertir el mapa a HTML para la plantilla
    }

    return render(request, 'aceptar_intercambio.html', context)

@login_required
def aceptar_intercambio(request, intercambio_id):
    turno_id = request.POST.get('turno_id')
    turno = get_object_or_404(Turno, id=turno_id)
    turno.turnos_disponibles-=1
    turno.save()
    intercambio = get_object_or_404(Intercambio, id=intercambio_id)
    intercambio.estado = 'Aceptado'
    intercambio.filial = turno.filial
    intercambio.turno = turno
    intercambio.codigo_intercambio_destinatario = get_random_string(10)
    intercambio.codigo_intercambio_solicitante = get_random_string(10)
    intercambio.save()
    send_mail(
                'Código de Intercambio',
                f'Aceptaste la solicitud de intercambio y se genero un código único para que presentes en la filial {intercambio.filial.nombre} en el turno de {turno.fecha}, tu código es : {intercambio.codigo_intercambio_destinatario}, perteneciente al intercambio con código: {intercambio.codigo_intercambio}.Por favor presentarse entre las 11 am y 20 pm. ',
             'ingecaritas@gmail.com',
                [intercambio.destinatario.mail],
                fail_silently=False,
    )
    send_mail(
                'Código de Intercambio',
                f'Se acepto tu solicitud de intercambio y se genero un código único para que presentes en la filial {intercambio.filial.nombre} en el turno de {turno.fecha}, tu código es : {intercambio.codigo_intercambio_destinatario}perteneciente al intercambio con código: {intercambio.codigo_intercambio}. Por favor presentarse entre las 11 am y 20 pm. ',
             'ingecaritas@gmail.com',
                [intercambio.solicitante.mail],
                fail_silently=False,
    )

    messages.success(request, 'Intercambio aceptado con éxito.')
                
    # Rechazar otras solicitudes sobre el mismo artículo
    rechazados=Intercambio.objects.filter(destinatario=intercambio.destinatario, 
                                           articulo_solicitado=intercambio.articulo_solicitado, 
                                           estado='Pendiente')
    for rechazado in rechazados:
        send_mail(
                'Intercambio',
                f'Se rechazo tu solicitud de intercambio pedida al usuario {rechazado.destinatario.nombre} para el articulo {rechazado.articulo_solicitado.Titulo} por este motivo: Se aceptó el intercambio a otro usuario.',
             'ingecaritas@gmail.com',
                [rechazado.solicitante.mail],
                fail_silently=False,
    )
        
    Intercambio.objects.filter(destinatario=intercambio.destinatario, 
                                           articulo_solicitado=intercambio.articulo_solicitado, 
                                           estado='Pendiente').exclude(id=intercambio.id).update(estado='Rechazado', motivo_rechazo='Aceptado otro intercambio.')

    return redirect('lista_intercambios')

@login_required
def rechazar_intercambio(request, intercambio_id):
    input_otro = False
    intercambio = get_object_or_404(Intercambio, id=intercambio_id)
    if request.method == 'POST':
        form = RechazarIntercambioForm(request.POST)
        if form.is_valid():
            motivo = request.POST.get('motivo_rechazo')
            otro_motivo = request.POST.get('otro_motivo')
            if motivo == 'Otro':
                motivo = otro_motivo
                print(motivo)
            intercambio = get_object_or_404(Intercambio, id=intercambio_id)
            intercambio.estado = 'Rechazado'
            intercambio.motivo_rechazo = motivo
            intercambio.save()
            send_mail(
                'Intercambio',
                f'Se rechazo tu solicitud de intercambio pedida al usuario {intercambio.destinatario.nombre} para el articulo {intercambio.articulo_solicitado.Titulo} por este motivo: {intercambio.motivo_rechazo}.',
             'ingecaritas@gmail.com',
                [intercambio.solicitante.mail],
                fail_silently=False,
    )
            messages.success(request, 'Intercambio rechazado con éxito.')
            return redirect('lista_intercambios')
            
    else:
        form = RechazarIntercambioForm()
    return render(request, 'rechazar_intercambio.html', {'form': form, 'intercambio': intercambio})