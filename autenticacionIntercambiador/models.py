from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

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

    USERNAME_FIELD = 'dni'

    objects = IntercambiadorManager()

    def __int__(self):
        return self.dni


