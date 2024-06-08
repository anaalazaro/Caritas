from django.urls import path
from .views import eliminar_articulo

urlpatterns=[
    path('eliminar_articulo/<int:articulo_id>/', eliminar_articulo, name='eliminarArticulo'),
]