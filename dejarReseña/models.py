from django.db import models
from app.models import CustomUser

class Reseña(models.Model):
    comentario = models.CharField(max_length=200)
    fecha = models.DateTimeField(auto_now_add=True)
    reseñante = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='reseñas_dejadas')
    reseñado = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='reseñas_recibidas')

    def __str__(self):
        return f'Reseña de {self.reseñante.username} a {self.reseñado.username}'