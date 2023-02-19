from __future__ import unicode_literals
from django.db import models

# Create your models here.

class lugares(models.Model):
    nombre = models.CharField(max_length = 50, blank = False, null = False)
    foto = models.ImageField()
    LvlEconomico = models.CharField(max_length = 50, blank = False, null = False)
    descripcion = models.CharField(max_length = 140, blank = False, null = False)
    ubicacion = models.CharField(max_length = 50, blank = False, null = False)

class usuario(models.Model):
    nombre = models.CharField(max_length = 100, blank = True, null = True)
    email = models.EmailField()
    contraseña = models.CharField(max_length = 50, blank = True, null = True)

    def __unicode__(self):
        return self.email
    
    def __str__(self):
        return self.email
