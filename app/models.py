from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    telefono = models.CharField(max_length=15)
    fechaNacimiento = models.DateField()
    dni = models.CharField(max_length=20, unique=True)
    passChange = models.BooleanField(default=False)
   # mail= models.EmailField()
    #puntaje= models.IntegerField(default=0)
    class Meta:
        app_label = 'app'
