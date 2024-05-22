from django.urls import path
from . import views

urlpatterns = [
    path('eliminar_filial/', views.eliminar_filial, name='eliminarFilial'),
]