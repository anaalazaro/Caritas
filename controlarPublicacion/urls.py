from django.urls import path
from .views import controlar_publicacion, aprobar_articulo, desaprobar_articulo

urlpatterns = [
    path('controlar_publicacion/<int:articulo_id>/', controlar_publicacion, name='controlar_publicacion'),
    path('aprobar_articulo/<int:articulo_id>/', aprobar_articulo, name='aprobar_articulo'),
    path('desaprobar_articulo/<int:articulo_id>/', desaprobar_articulo, name='desaprobar_articulo'),
]
