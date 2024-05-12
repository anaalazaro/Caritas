from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ArticuloForm
from django.core.mail import send_mail
from django.contrib.auth.models import User

@login_required
def agregar_articulo(request):
    if request.method == 'POST':
        form = ArticuloForm(request.POST, request.FILES)
        if form.is_valid():
            articulo = form.save(commit=False)
            articulo.usuario = request.user
            articulo.pendiente = True  # Establece el estado del artículo como pendiente
            articulo.save()
            messages.success(request, 'La publicación del artículo ha quedado pendiente a la aprobación del ayudante.')
            # Enviar notificación al ayudante
        #    ayudante = User.objects.filter(groups__name='Ayudantes').first()  # Suponiendo que los ayudantes estén en un grupo llamado 'Ayudantes'
         #   if ayudante:
          #      send_mail(
           #         'Nuevo artículo pendiente',
             #       f'Hola {ayudante.username}, hay un nuevo artículo pendiente de revisión.',
            #        'from@example.com',
              #      [ayudante.email],
               #  fail_silently=True,
              #  )
            return redirect('http://127.0.0.1:8000/')  # Redirecciona al usuario a la página principal después de agregar el artículo
    else:
        form = ArticuloForm()
    return render(request, 'cargarArticulo.html', {'form': form})
