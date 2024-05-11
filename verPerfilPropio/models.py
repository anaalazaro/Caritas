from django.db import models
from django.contrib.auth.models import AbstractUser

class Intercambiador(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    score = models.IntegerField(default=0)  # Puntaje del usuario
