from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def main(request):
    return render(request, 'main.html')

def recomendaciones(request):
    return render(request, 'recomendaciones.html')

def foro(request):
    return render(request, 'ForoComunidad.html')