from django.urls import path
from . import views

urlpatterns = [
    path('change_desired_password/', views.change_desired_password, name='change_desired_password'),
    path('cambio_exitoso/', views.change_desired_password, name='cambio_exitoso'),
]
