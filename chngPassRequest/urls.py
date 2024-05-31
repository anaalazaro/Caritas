from django.urls import path
from . import views

urlpatterns = [
    path('change_password/', views.change_password_request, name='change_password'),
    path('change_password/confirm/', views.change_password_confirm, name='change_password_confirm'),
]