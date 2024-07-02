from django.urls import path
from . import views

urlpatterns = [
    path('ver_reseñas/<int:user_id>/', views.ver_reseñas, name='ver_reseñas'),
]
