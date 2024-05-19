from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    nombre = models.CharField(max_length=100, default='')  
    apellido = models.CharField(max_length=100, default='')  
    mail = models.EmailField(default='')
    telefono = models.CharField(max_length=15)
    dni = models.IntegerField(max_length=20, unique=True)
    fechaNacimiento = models.DateField()
    puntaje= models.IntegerField(default=0)
    class Meta:
        app_label = 'app'
