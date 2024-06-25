from django.urls import path
from . import views

urlpatterns = [
    path('articulos_rechazados/', views.mostrarArticulosRechazados, name='articulos_rechazados'),
]