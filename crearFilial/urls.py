from django.urls import path
from . import views

urlpatterns = [
    path('agregar_filial/', views.agregar_filial, name='agregarFilial'),
]