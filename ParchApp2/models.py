from __future__ import unicode_literals
from django.db import models

# Create your models here.
Economy = [('menor que 50k','menor que 50k'), ('entre 50k y 150k','entre 50k y 150k'), ('mas de 150k','mas de 150k')]
Zone = [('Envigado','Envigado'),('Poblado','Poblado')]
Category = [('Discoteca','Discoteca'),('Restaurante','Restaurante'),('Mirador','Mirador')]
Age = [('menor de edad','menor de edad'),('mayor de edad','mayor de edad')]

class lugar(models.Model):
    nombre = models.CharField(max_length = 50, blank = True, null = True)
    #foto = models.ImageField()
    LvlEconomico = models.CharField(max_length=50, blank = True, null = True, choices=Economy)
    descripcion = models.CharField(max_length = 140, blank = True, null = True)
    Zona = models.CharField(max_length = 50, blank = True, null = True, choices= Zone)
    categoria = models.CharField(max_length= 50, blank = True, null = True, choices= Category)
    edad = models.CharField(max_length=50, blank = True, null = True, choices= Age)
    
    def __str__(self):
        
        return self.categoria