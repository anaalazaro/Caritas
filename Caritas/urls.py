"""
URL configuration for Caritas project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app import views
from cargarArticulo.views import agregar_articulo
from verArticulosPendientes.views import mostrar_articulos_pendientes
from controlarPublicacion.views import controlar_publicacion



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.hello),
    path('register/', views.registro, name='register'),
    path('cargarArticulo/', agregar_articulo, name='cargar_articulo'),
    path('articulos_pendientes/', mostrar_articulos_pendientes, name='mostrar_articulos_pendientes'),
     path('controlar_publicacion/<int:articulo_id>/', controlar_publicacion, name='controlar_articulo'),
]
