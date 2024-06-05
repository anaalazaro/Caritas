from django.urls import path
from verIntercambiadores import views

urlpatterns = [
    path('verIntercambiadores/', views.ver_intercambiadores, name='verIntercambiadores'),
]