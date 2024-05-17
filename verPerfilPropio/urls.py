from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.view_profile, name='view_profile'),  # Ruta para ver el perfil del usuario
    # Agrega más rutas según sea necesario para otras vistas de tu aplicación
]
