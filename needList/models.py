from django.db import models
from app.models import CustomUser
from cargarArticulo.models import Articulo

class NeedList(models.Model):
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE, db_constraint=False)
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE, db_constraint=False)

