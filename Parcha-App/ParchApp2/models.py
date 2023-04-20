from __future__ import unicode_literals
from django.db import models

# Create your models here.
Economy = [('menor que 50k','menor que 50k'), ('entre 50k y 150k','entre 50k y 150k'), ('mas de 150k','mas de 150k')]
Zone = [('Envigado','Envigado'),('Poblado','Poblado')]
Category = [('Discoteca','Discoteca'),('Restaurante','Restaurante'),('Mirador','Mirador'),('Centro Comercial','Centro Comercial')]
Age = [('menor de edad','menor de edad'),('mayor de edad','mayor de edad')]

class lugar(models.Model):
    nombre = models.CharField(max_length = 50,default='x')
    foto = models.ImageField(upload_to='Parcha-App/images/',default='')
    LvlEconomico = models.CharField(max_length=50, choices=Economy,default='')
    descripcion = models.CharField(max_length = 500,default='')
    Zona = models.CharField(max_length = 50, choices= Zone,default='')
    categoria = models.CharField(max_length= 50, choices= Category,default='')
    edad = models.CharField(max_length=50, choices= Age,default='')
    
    def __str__(self):
        
        return self.nombre