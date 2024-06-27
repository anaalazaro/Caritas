from django.db import models
from app.models import CustomUser
from datetime import datetime, timedelta

class Filial(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    ayudante = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)
    latitud = models.FloatField(null=True, blank=True)
    longitud = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.nombre

    def generar_turnos(self):
        fecha_actual = datetime.now()
        fecha_proximo_mes = fecha_actual + timedelta(days=360)

        while fecha_actual <= fecha_proximo_mes:
            if fecha_actual.weekday() in [5, 6]:  # Sábado es 5 y domingo es 6
                Turno.objects.create(
                    filial=self,
                    fecha=fecha_actual,
                    turnos_disponibles=50
                )
            fecha_actual += timedelta(days=1)

    @classmethod
    def generar_turnos_nueva_filial(cls, sender, instance, created, **kwargs):
        if created:
            instance.generar_turnos()

models.signals.post_save.connect(Filial.generar_turnos_nueva_filial, sender=Filial)


class Turno(models.Model):
    filial = models.ForeignKey(Filial, related_name='turnos', on_delete=models.CASCADE)
    fecha = models.DateField()
    turnos_disponibles = models.PositiveIntegerField()

    class Meta:
        unique_together = ('filial', 'fecha')

    def __str__(self):
        return f"{self.filial.nombre} - {self.fecha} - Turnos disponibles: {self.turnos_disponibles}"
