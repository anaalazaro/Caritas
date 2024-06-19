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
from verAyudantesRegistrados.views import ver_ayudantes, confirmar_eliminar_ayudante
from editarPerfilAdministrador.views import editar_perfil
from buscarArticulo.views import buscar_articulos
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
from bloquearUsuario.views import bloquear_usuario 
from bloquearUsuario.views import lista_usuarios
from needList import views as needListViews
from solicitarIntercambio.views import solicitar_intercambio
from controlarIntercambio.views import controlar_intercambio


from . import pendienteBloqueo

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
  path('', include('crearFilial.urls')),
  path('', include('listarFiliales.urls')),
  path('', include('eliminarFilial.urls')),
  path('', include('verIntercambiadores.urls')),
  path('confirmar_eliminar_cuenta/', viewsInicio.confirmar_eliminar_cuenta, name='confirmar_eliminar_cuenta'), 
  path('menuPrincipal/', viewsInicio.mostrar, name='menuPrincipal'),# Incluye las URLs de verPerfilPropio
  path('detalleArticulo//<int:articulo_id>/', viewsDetalle.mostrarDetalle, name='detalle'),
  path('ordenarAlfabeticamente', viewsInicio.mostrarArticulosOrdenados, name='ordenados'),
  path('verOtroUsuario/<int:user_id>/', other_profile_views.view_other_profile, name= 'ver_otro_usuario'),
  path('eliminarCuenta/<int:user_id>/', eliminar_cuenta_views.delete_account, name='eliminar_cuenta'),
  path('listarEliminados', viewsInicio.mostrarArticulosAEliminar, name= 'listarAEliminar'),
  path('eliminarArticulo/<int:articulo_id>/', viewsInicio.eliminarArticulo, name='eliminarArticulo'), 
    path('verAyudantes/', ver_ayudantes,name = 'verAyudantes'),
    path('inicioAdmin/', viewsInicio.inicioAdmin ,name = 'inicioAdmin'),
    path('misArticulos/', ver_articulos, name='verArticulos'),
    path('verArticulos/<int:user_profile_id>/', other_profile_views.verProductos, name='productos_del_usuario'),
    path('articulos/', buscar_articulos, name='articulos'),
  #path('login/', autenticacion_views.login_view, name='login'),
 #path('perfil_propio/', perfil_views.view_profile, name='perfil_propio'),
 path('inicioAyudante/', viewsInicio.inicioAyudante, name='inicioAyudante'),
 path('marcar_leida/<int:notification_id>/', viewsInicio.marcar_leida, name='marcar_leida'),
 path('bloquear_usuario/<int:user_id>/', bloquear_usuario, name='bloquear_usuario'),
 path('usuarios/', lista_usuarios, name='lista_usuarios'), 
  path('agregarANeedList/<int:articulo_id>/', needListViews.agregarArticuloANeedList, name= 'agregarANeedList'),
 path('verNeedList', needListViews.verArticulosEnLaNeedList, name='verNeedList'),
 path('borrarDeNeedList/<int:articulo_id>/', needListViews.borrarArticuloDeNeedList, name='borrarDeNeedList'),
 path('confirmar_eliminar_articulo/<int:articulo_id>/', needListViews.confirmar_eliminar_articulo, name='confirmar_eliminar_articulo'),
 path('solicitarIntercambio/<int:articulo_id>/', solicitar_intercambio, name='solicitar_intercambio'),
#  path('controlar_intercambio/<int:intercambio_id>', controlar_intercambio, name='controlar_intercambio'),
 path('listaIntercambios/', viewsInicio.mostrarIntercambios, name='lista_intercambios'),
 path('listaIntercambiosPendientes/', viewsInicio.mostrarIntercambiosPendientes, name='lista_intercambios_pendientes'),
 path('', include('controlarIntercambio.urls')),
  path('', include('eliminarArticulo.urls')),
 path('listadoABloquear', pendienteBloqueo.verUsuariosParaBloquear, name='verABloquear' ),
 path('listadoBloqueados', pendienteBloqueo.verUsuariosBloqueados, name='verBloqueados' ),
 path('bloquearPorPublicacion/<int:articulo_id>/<int:user_id>/', controlar_publicacionViews.bloquearUsuarioPorPublicacion, name='bloquearUsuarioPorInadecuado'),
 path('confirmarBloqueo/<int:articulo_id>/<int:user_id>/', controlar_publicacionViews.confirmar_bloquear, name='confirmar'),
 path('confirmar_eliminar_ayudante/<int:user_id>', confirmar_eliminar_ayudante, name='confirmar_eliminar_ayudante'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


