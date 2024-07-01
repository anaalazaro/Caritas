from django.urls import path
from . import views

urlpatterns = [
    path('donar/', views.donar, name='donar'),
]
