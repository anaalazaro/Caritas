from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from cargarArticulo.models import Articulo
from app.forms import CustomUser
from solicitarIntercambio.models import Intercambio
from django.db.models import Q
from django.core.mail import send_mail

def eliminar_articulo(request, articulo_id):
   articulo = get_object_or_404(Articulo, pk=articulo_id)
   if request.method == 'POST':
      intercambio = Intercambio.objects.filter(
        Q(articulo_ofrecido=articulo_id) | Q(articulo_solicitado=articulo_id),
        estado='Aprobado'
       ).first()
      if intercambio is not None:
         send_mail(
                  'Intercambio',
                   f'Se canceló el intercambio que solicisitaste al usuario {intercambio.destinatario.nombre} para el articulo {intercambio.articulo_solicitado.Titulo} para el día {intercambio.turno.fecha }por este motivo: Se eliminó el artículo que solicitaste',
                   'ingecaritas@gmail.com',
                  [intercambio.solicitante.mail],
                  fail_silently=False,
            )  
        #BORRAR LOGICAMENTE
      articulo.borrado= True
      articulo.save()
      messages.success(request, 'Artículo eliminado exitosamente')  # Envía el mensaje de éxito
      if request.user.roles == 'admin':
         return redirect('listarAEliminar')  # Reemplaza 'lista_articulos' con el nombre de tu URL de lista de artículos
      else:
         return redirect('verArticulos') 
   return render(request, 'eliminar_articulo.html', {'articulo': articulo})