from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    nombre = models.CharField(max_length=100, default='')  
    apellido = models.CharField(max_length=100, default='')  
    mail = models.EmailField(default='')
    telefono = models.CharField(max_length=15)
    dni = models.IntegerField(max_length=20, unique=True,default=0)
    fechaNacimiento = models.DateField(default='2000-01-01')
    puntaje= models.IntegerField(default=0)
    passChange = models.BooleanField(default=False)
  
    # Campos con opciones
    OPCIONES_ROL = [
        ('usuario', 'Usuario intercambiador'),
        ('admin', 'Administrador'),
        ('ayudante', 'Usuario ayudante'),
    ]
    roles = models.CharField(max_length=8, choices=OPCIONES_ROL, default='admin')
   # mail= models.EmailField()
    #puntaje= models.IntegerField(default=0)
     # Nuevo campo
    is_blocked = models.BooleanField(default=False)
    pendiente_bloqueo= models.BooleanField (default=False)
    motivo_bloqueo = models.CharField(max_length=255, blank=True, null=True)
    failed_login_attempts= models.IntegerField(default=0)
    
    # Nuevos campos para contador de solicitudes pendientes
    solicitudes_pendientes_enviadas = models.IntegerField(default=0)
    solicitudes_pendientes_recibidas = models.IntegerField(default=0)
    def actualizar_solicitudes_pendientes(self):
        self.solicitudes_pendientes_enviadas = self.solicitudes_enviadas.filter(estado='pendiente').count()
        self.solicitudes_pendientes_recibidas = self.solicitudes_recibidas.filter(estado='pendiente').count()
        self.save()

    cantidad_rechazos_publicacion=models.IntegerField(default=0)
    class Meta:
        app_label = 'app'
