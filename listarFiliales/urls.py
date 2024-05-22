from django.urls import path
from . import views

urlpatterns = [
    path('listar_filiales/', views.listar_filiales, name='listarFiliales'),
]