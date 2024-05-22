from django.urls import path
from . import views

urlpatterns = [
    path('eliminar_filial/<int:filial_id>/', views.eliminar_filial, name='eliminarFilial'),
]