from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class Intercambiador(AbstractUser):
    phone_number = models.CharField (max_length=15, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    score = models.IntegerField(default=0)  # Puntaje del usuario
    groups = models.ManyToManyField(Group, related_name='ver_perfil_propio_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='ver_perfil_propio_permissions')
