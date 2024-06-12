from django.urls import path
from .views import aceptar_intercambio, rechazar_intercambio,controlar_intercambio

urlpatterns = [
    path('aceptar_intercambio/<int:intercambio_id>/', aceptar_intercambio, name='aceptar_intercambio'),
    path('rechazar_intercambio/<int:intercambio_id>/', rechazar_intercambio, name='rechazar_intercambio'),
    path('controlar_intercambio/<int:intercambio_id>/', controlar_intercambio, name='controlar_intercambio')
]
