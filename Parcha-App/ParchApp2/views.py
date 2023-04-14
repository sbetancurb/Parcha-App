from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.db.models import Q
from ParchApp2.forms import *

#Views of the project
def home(request):
    return render(request, 'Home.html')

def recomendaciones(request):
    edad = request.GET.get('Age')
    zona = request.GET.get('Zone')
    categoria = request.GET.get('Category')
    economia = request.GET.get('Economy')
    lugares = lugar.objects.all()

    if (edad and zona and categoria and economia):
        lugares = lugar.objects.filter(
        Q(edad__icontains = edad) |
        Q(Zona__icontains = zona) |
        Q(LvlEconomico__icontains = economia) |
        Q(categoria__icontains = categoria)
    ).distinct()

    return render(request,"recomendaciones.html",{'lugares':lugares})

def foro(request):
    return render(request, 'ForoComunidad.html')

def login(request):
    return render(request, 'registration/login.html')

def salida(request):
    logout(request)
    return redirect('/')