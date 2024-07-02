from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from app.models import CustomUser
from .models import Reseña
from .forms import ReviewForm
from solicitarIntercambio.models import Intercambio

@login_required
def dejar_reseña(request, intercambio_id, user_id):
    other_user = get_object_or_404(CustomUser, id=user_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.reseñante = request.user  # Aquí asumimos que request.user es un CustomUser
            review.reseñado = other_user
            review.save()
            intercambio = get_object_or_404(Intercambio, id=intercambio_id)
            if(intercambio.destinatario_id == request.user.id):
                intercambio.reseña_destinatario=True
            else:
                intercambio.reseña_solicitante=True
            intercambio.save()
            return redirect('lista_intercambios')  # Ajusta según la URL de detalle de usuario
    else:
        form = ReviewForm()

    return render(request, 'dejar_reseña.html', {'user_profile': other_user, 'form': form})
