from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, Group, Permission
from django.db import models
from django import forms

class IntercambiadorManager(BaseUserManager):
    def create_user(self, dni, password=None, **extra_fields):
        if not dni:
            raise ValueError("El DNI es obligatorio")
        user = self.model(dni=dni, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, dni, password=None, **extra_fields):
        user = self.create_user(dni, password, **extra_fields)
        user.is_admin = True
        user.save(using=self._db)
        return user

class Intercambiador(AbstractBaseUser):
    dni = models.CharField(max_length=10, unique=True)
    failed_login_attempts = models.IntegerField(default=0)
    is_locked = models.BooleanField(default=False)
    # Solución para evitar el conflicto en los accesores inversos
    groups = models.ManyToManyField(Group, related_name='intercambiador_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='intercambiador_user_permissions')

    # Campo para la imagen de perfil con ImageField
    profile_picture = models.ImageField(upload_to='profile_pictures', null=True, blank=True)

    USERNAME_FIELD = 'dni'

    objects = IntercambiadorManager()

    def int(self):
        return self.dni

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())

class CustomUser(AbstractBaseUser):
    # Otros campos de tu modelo CustomUser

    # Solución para evitar el conflicto en los accesores inversos
    groups = models.ManyToManyField(Group, related_name='customuser_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='customuser_user_permissions')
