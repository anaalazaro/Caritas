from django.db import models
from app.models import CustomUser
from cargarArticulo.models import Articulo
from crearFilial.models import Filial,Turno


class Intercambio(models.Model):
    solicitante = models.ForeignKey(CustomUser, related_name='solicitudes_enviadas', on_delete=models.CASCADE)
    destinatario = models.ForeignKey(CustomUser, related_name='solicitudes_recibidas', on_delete=models.CASCADE)
    articulo_solicitado = models.ForeignKey(Articulo, related_name='solicitudes_donde_es_solicitado', on_delete=models.CASCADE)
    articulo_ofrecido = models.ForeignKey(Articulo, related_name='solicitudes_donde_es_ofrecido', on_delete=models.CASCADE)
    fecha_solicitud = models.DateTimeField(auto_now_add=True)

    # Campos con opciones para un estado
    OPCIONES_ESTADO = [
        ('Pendiente', 'Articulo Pendiente'),
        ('Aceptado', 'Articulo Aceptado'),
        ('Rechazado', 'Rechazado'),
        ('Efectuado', 'Efectuado'),
        ('No efectuado', 'No efectuado'),
    ]
    estado = models.CharField(max_length=20, choices=OPCIONES_ESTADO,default='Pendiente')
    codigo_intercambio= models.CharField(max_length=15, blank=True, null=True)
    codigo_intercambio_destinatario = models.CharField(max_length=10, blank=True, null=True)
    codigo_intercambio_solicitante = models.CharField(max_length=10, blank=True, null=True)
    motivo_rechazo = models.TextField(blank=True, null=True)
    filial = models.ForeignKey(Filial, on_delete=models.CASCADE,blank=True, null=True)
    turno = models.ForeignKey(Turno,on_delete=models.CASCADE,blank=True, null=True) 
    class Meta:
        verbose_name_plural = "Intercambios"
