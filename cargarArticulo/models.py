from django.db import models
from Caritas import settings

class Articulo(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    Foto = models.ImageField(upload_to='articulos/')
    Categoria = models.CharField(max_length=100)
    Titulo = models.CharField(max_length=200)
    Descripcion = models.TextField()
    Estado = models.CharField(max_length=20)
    pendiente = models.BooleanField(default=True)
    aprobado= models.BooleanField(default=False)