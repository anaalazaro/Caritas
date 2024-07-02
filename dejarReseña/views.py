from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from app.models import CustomUser
from .models import Reseña
from .forms import ReviewForm

@login_required
def dejar_reseña(request, user_id):
    other_user = get_object_or_404(CustomUser, id=user_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.reseñante = request.user  # Aquí asumimos que request.user es un CustomUser
            review.reseñado = other_user
            review.save()
            return redirect('ver_otro_usuario', user_id=user_id)  # Ajusta según la URL de detalle de usuario
    else:
        form = ReviewForm()

    return render(request, 'dejar_reseña.html', {'user_profile': other_user, 'form': form})
