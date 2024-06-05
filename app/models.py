from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    nombre = models.CharField(max_length=100, default='')  
    apellido = models.CharField(max_length=100, default='')  
    mail = models.EmailField(default='')
    telefono = models.CharField(max_length=15)
    dni = models.IntegerField(max_length=20, unique=True,default=0)
    fechaNacimiento = models.DateField(default='2000-01-01')
    puntaje= models.IntegerField(default=0)
    passChange = models.BooleanField(default=False)
    filial = models.CharField(max_length=20, default='')
    # Campos con opciones
    OPCIONES_ROL = [
        ('usuario', 'Usuario intercambiador'),
        ('admin', 'Administrador'),
        ('ayudante', 'Usuario ayudante'),
    ]
    roles = models.CharField(max_length=8, choices=OPCIONES_ROL, default='admin')
   # mail= models.EmailField()
    #puntaje= models.IntegerField(default=0)
     # Nuevo campo
    is_blocked = models.BooleanField(default=False)
    pendiente_bloqueo= models.BooleanField (default=False)
    motivo_bloqueo = models.CharField(max_length=255, blank=True, null=True)
    failed_login_attempts= models.IntegerField(default=0)
    class Meta:
        app_label = 'app'
