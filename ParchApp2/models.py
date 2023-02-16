from django.db import models

# Create your models here.

class lugares(models.Model):
    nombre = models.CharField(max_length = 50, blank = False, null = False)
    foto = models.ImageField()
    LvlEconomico = models.CharField(max_length = 50, blank = False, null = False)
    descripcion = models.CharField(max_length = 140, blank = False, null = False)
    ubicacion = models.CharField(max_length = 50, blank = False, null = False)

