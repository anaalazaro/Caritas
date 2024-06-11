from django.db import models
from app.models import CustomUser

class Filial(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    ayudante = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, db_constraint=False,null=True, blank=True)

    def __str__(self):
        return self.nombre
