from django.db import models
from app.models import CustomUser

class Articulo(models.Model):
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE, db_constraint=False)
    Foto = models.ImageField(upload_to='articulos/')
    Categoria = models.CharField(max_length=100)
    Titulo = models.CharField(max_length=200)
    Descripcion = models.TextField()
    Estado = models.CharField(max_length=20)
    pendiente = models.BooleanField(default=True)
    aprobado = models.BooleanField(default=False)