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
from django.conf import settings
from django.conf.urls.static import static
from app import views
from cargarArticulo.views import agregar_articulo
from verArticulosPendientes.views import mostrar_articulos_pendientes
from controlarPublicacion.views import controlar_publicacion
from autenticacionIntercambiador import views as autenticacion_views
from verPerfilPropio import views as perfil_views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.hello),
    path('register/', views.registro, name='register'),
    path('cargarArticulo/', agregar_articulo, name='cargar_articulo'),
    path('articulos_pendientes/', mostrar_articulos_pendientes, name='mostrar_articulos_pendientes'),
     path('controlar_publicacion/<int:articulo_id>/', controlar_publicacion, name='controlar_articulo'),

  path('register/', views.registro, name='register'),
  path('login/', autenticacion_views.login_view, name='login'),  # Incluye las URLs de autenticacionIntercambiador
  path('perfil_propio/', perfil_views.view_profile, name='perfil_propio'),  # Incluye las URLs de verPerfilPropio
  #path('login/', autenticacion_views.login_view, name='login'),
 #path('perfil_propio/', perfil_views.view_profile, name='perfil_propio'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

