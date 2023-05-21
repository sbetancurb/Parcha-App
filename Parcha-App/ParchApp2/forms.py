from django import forms
from ParchApp2.models import *

class ProductoForm(forms.Form):
    Edad = forms.CharField(label="Edad", max_length=50)
    Tipo = forms.CharField(label="Tipo", max_length=50)
    Zona = forms.CharField(label="Zona", max_length=50)
    Eco = forms.CharField(label="Eco", max_length=50)
