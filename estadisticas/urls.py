from django.urls import path
from . import views

urlpatterns = [
    path('estadisticas/', views.estadisticas_periodo_tiempo, name='estadisticas'),
    path('estadisticasPorFilial/', views.estadisticas_por_filial, name='estadisticasPorFilial'),
]