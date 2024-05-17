from django.urls import path
from . import views

urlpatterns = [
    path('login_otp', views.login_otp, name='login_otp'),
    path('otp', views.otp, name='otp'),
    path('main/', views.main_view, name='main'),
]