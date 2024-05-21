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
from registrarAyudante.views import registro
from verAyudantesRegistrados.views import ver_ayudantes
from editarPerfilAdministrador.views import editar_perfil
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from django.views.generic import RedirectView
from app import views
from . import views as viewsInicio
from cargarArticulo import views as cargarArticuloViews
from verArticulosPendientes.views import mostrar_articulos_pendientes
from controlarPublicacion import views as controlar_publicacionViews
from autenticacionIntercambiador import views as autenticacion_views
from verPerfilPropio import views as perfil_views
from verDetalleDeArticulo import views as viewsDetalle
from verOtroUsuario import views as other_profile_views
from eliminarCuenta import views as eliminar_cuenta_views
from verArticulosPropios.views import ver_articulos

urlpatterns = [
    path('', RedirectView.as_view(url='Inicio/', permanent=True)),
    path('admin/', admin.site.urls),
    path('registrar/', registro,name = 'registro'),
    path('editarPerfil/<int:usuario_id>/', editar_perfil,name = 'editarPerfilAdmin'),
    path('Inicio/', viewsInicio.hello, name='inicio'),
    path('register/', views.registro, name='register'),
    path('cargarArticulo/', cargarArticuloViews.cargar_articulo, name='cargar_articulo'),
    path('articulos_pendientes', mostrar_articulos_pendientes, name='mostrar_articulos_pendientes'),
    path('controlar_publicacion/<int:articulo_id>/', controlar_publicacionViews.controlar_publicacion, name='controlar_articulo'),
 path('desaprobar/<int:articulo_id>/', controlar_publicacionViews.desaprobar_articulo, name="desaprobar"),
   path('aprobar/<int:articulo_id>/', controlar_publicacionViews.aprobar_articulo, name="aprobar"),
   path('mostrar_por_categoria/', viewsInicio.mostrarPorCategoria, name='mostrar_por_categoria'),
  path('register/', views.registro, name='register'),
  path('login/', autenticacion_views.login_view, name='login'),  # Incluye las URLs de autenticacionIntercambiador
  path('perfil_propio/', perfil_views.view_profile, name='perfil_propio'),  
  path('', include('ayudanteAuth.urls')),
  path('', include('chngPassRequest.urls')),
  path('', include('changePassword.urls')),
  path('', include('logout.urls')),
  path('menuPrincipal/', viewsInicio.mostrar, name='menuPrincipal'),# Incluye las URLs de verPerfilPropio
  path('detalleArticulo//<int:articulo_id>/', viewsDetalle.mostrarDetalle, name='detalle'),
  path('ordenarAlfabeticamente', viewsInicio.mostrarArticulosOrdenados, name='ordenados'),
  path('verOtroUsuario/<int:user_id>/', other_profile_views.view_other_profile, name= 'ver_otro_usuario'),
  path('eliminarCuenta/<int:user_id>/', eliminar_cuenta_views.delete_account, name='eliminar_cuenta'),
  path('verArticulos/<int:user_profile_id>/', other_profile_views.verProductos, name='productos_del_usuario'),
    path('verAyudantes/', ver_ayudantes,name = 'verAyudantes'),
    path('inicioAdmin/', viewsInicio.inicioAdmin ,name = 'inicioAdmin'),
    path('misArticulos/', ver_articulos, name='verArticulos'),
  #path('login/', autenticacion_views.login_view, name='login'),
 #path('perfil_propio/', perfil_views.view_profile, name='perfil_propio'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
