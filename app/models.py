from django.db import models

# Create your models here.
# accounts/models.py

from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # Agrega campos adicionales si es necesario
    fecha_nacimiento = models.DateField()
    dni = models.CharField(max_length=10, unique=True)
    telefono = models.CharField(max_length=15)
    filial = models.CharField(max_length=20)
    
    # Campos con opciones
    OPCIONES_ROL = [
        ('usuario', 'Usuario intercambiador'),
        ('admin', 'Administrador'),
        ('ayudante', 'Usuario ayudante'),
    ]
    roles = models.CharField(max_length=8, choices=OPCIONES_ROL, default='usuario')
    class Meta:
        app_label = 'app'
    # Establece grupos y permisos de usuario como campos no relacionales
    # groups = None
    # user_permissions = None