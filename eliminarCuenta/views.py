from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import transaction
from app.models import CustomUser
from solicitarIntercambio.models import Intercambio
from django.db.models import Q
from django.core.mail import send_mail
from crearFilial.models import Filial

def delete_account(request, user_id):
    usuario = CustomUser.objects.get(pk=user_id)
    usuario_actual = request.user
    rol = usuario_actual.roles
    if 'admin' in rol:
        filial_ayudante= Filial.objects.get(ayudante=user_id)
        intercambios_filial = Intercambio.objects.filter(filial=filial_ayudante, estado='Aceptado')
        if not intercambios_filial.exists():
            usuario.borrado=True
            usuario.save()
            filial_ayudante.ayudante=None
            filial_ayudante.save()
            messages.success(request, 'Se eliminó al ayudante exitosamente')
        else:
            messages.success(request, 'No puedes eliminar al ayudante ya que esta asociado a una filial con intercambios pendientes a efectuar')
        return redirect('verAyudantes')   
    intercambios_solicitante= Intercambio.objects.filter(solicitante= user_id, estado='Aprobado')
    intercambios_destinatario= Intercambio.objects.filter(destinatario= user_id, estado='Aprobado')
    if intercambios_solicitante.exists() :
        for destinatario_usuario in intercambios_solicitante:
            send_mail(
                 'Intercambio',
                    f'Se canceló el intercambio pactado con el intercambiador{destinatario_usuario.solicitante.nombre} para el articulo {destinatario_usuario.articulo_ofrecido.Titulo} para el día {destinatario_usuario.turno.fecha }por este motivo: Se dió de baja la cuenta del usuario {destinatario_usuario.solicitante.nombre}' ,
                    'ingecaritas@gmail.com',
                    [destinatario_usuario.destinatario.mail],
                    fail_silently=False,
            )
    if intercambios_destinatario.exists():
        for solicitante_usuario in intercambios_destinatario:
            send_mail(
                 'Intercambio',
                    f'Se canceló el intercambio pactado con el intercambiador{solicitante_usuario.destinatario.nombre} para el articulo {solicitante_usuario.articulo_ofrecido.Titulo} para el día {solicitante_usuario.turno.fecha }por este motivo: Se dió de baja la cuenta del usuario {solicitante_usuario.destinatario.nombre}' ,
                    'ingecaritas@gmail.com',
                    [solicitante_usuario.destinatario.mail],
                    fail_silently=False,
            )
    usuario.borrado=True
    usuario.save()
    messages.success(request, 'La cuenta se ha eliminado exitosamente')
    if 'admin' in rol:
        return redirect('verAyudantes')
    else:
        return redirect('inicio')
    