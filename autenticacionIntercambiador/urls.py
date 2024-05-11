from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),  # Ruta para el inicio de sesión
]
