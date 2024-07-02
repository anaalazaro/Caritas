from django.urls import path
from . import views

urlpatterns = [
    path('dejar_reseña/<int:intercambio_id>/<int:user_id>/', views.dejar_reseña, name='dejar_reseña'),
]
