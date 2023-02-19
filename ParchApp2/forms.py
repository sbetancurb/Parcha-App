from django import forms

class RegForms(forms.Form):
    nombre = forms.CharField(max_length=100)
    email = forms.EmailField()
    contraseña = forms.CharField(max_length=100)