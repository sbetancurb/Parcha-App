from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.db.models import Q
from ParchApp2.forms import *
import matplotlib.pyplot as plt
import os

#Views of the project
def home(request):
    all_objects = cuestionario.objects.all()
    dict = {
        'Envigado' : 0,
        'Poblado' : 0,
        'Default' : 0
    }
    for obj in all_objects:
        dict[obj.Zona] = dict[obj.Zona] + 1
    keys = dict.keys()
    values = dict.values()
    plt.pie(values, labels=keys, autopct='%1.1f%%')
    plt.title('Cuestionarios')
    plt.axis('equal')
    plot_path = os.path.join('static', 'plot.png')
    plt.savefig(plot_path)
    plt.close()

    dict2 = {
        'Discoteca' : 0,
        'Restaurante' : 0,
        'Centro Comercial' : 0,
        'Mirador' : 0
    }
    for obj in all_objects:
        dict2[obj.Tipo] = dict2[obj.Tipo] + 1
    fig, ax = plt.subplots()
    ax.bar(dict2.keys(), dict2.values())
    plot_path = os.path.join('static', 'plot2.png')
    plt.savefig(plot_path)
    plt.close()

    dict3 = {
        'menor que 50k' : 0,
        'entre 50k y 150k' : 0,
        'mas de 150k' : 0,
        'Default' : 0
    }
    for obj in all_objects:
        dict3[obj.Eco] = dict3[obj.Eco] + 1
    fig, ax = plt.subplots()
    ax.bar(dict3.keys(), dict3.values())
    plot_path = os.path.join('static', 'plot3.png')
    plt.savefig(plot_path)
    plt.close()

    print(dict)
    print(dict2)
    print(dict3)

    return render(request, 'Home.html', {'data' : dict})

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
