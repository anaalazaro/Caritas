from django.shortcuts import render, get_object_or_404
from app.models import CustomUser
from dejarReseña.models import Reseña

def ver_reseñas(request, user_id):
    # Obtener el usuario cuyas reseñas queremos ver
    user = get_object_or_404(CustomUser, id=user_id)

    # Obtener todas las reseñas donde este usuario es el receptor
    reseñas = Reseña.objects.filter(reseñado=user)

    context = {
        'user_profile': user,
        'reseñas': reseñas,
    }

    return render(request, 'ver_reseñas.html', context)
