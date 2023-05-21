from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.db.models import Q
from ParchApp2.forms import *

#Views of the project
def home(request):
    return render(request, 'Home.html')

@login_required
def recomendaciones(request):
    
    form = ProductoForm()

    edad = request.POST.get('Age')
    zona = request.POST.get('Zone')
    categoria = request.POST.get('Category')
    economia = request.POST.get('Economy')
    lugares = lugar.objects.all()

    if (edad and zona and categoria and economia):
        lugares = lugar.objects.filter(
        Q(edad__icontains = edad) |
        Q(Zona__icontains = zona) |
        Q(LvlEconomico__icontains = economia) |
        Q(categoria__icontains = categoria)
    ).distinct()
        
    
    if request.method == 'POST':
        print(request.POST)
        form = ProductoForm(request.POST)

        if form.is_valid():
            print('invalido')

        else:
            print('valido')
            
            product = cuestionario()

            product.Edad = request.POST.get('Age')
            product.Tipo = request.POST.get('Category')
            product.Zona = request.POST.get('Zone')
            product.Eco = request.POST.get('Economy')

            product.save()

    return render(request,"recomendaciones.html",{'lugares':lugares})
