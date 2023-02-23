from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

#Views of the project
@login_required
def home(request):
    return render(request, 'Home.html')

def recomendaciones(request):
    return render(request, 'recomendaciones.html')

def foro(request):
    return render(request, 'ForoComunidad.html')

def login(request):
    return render(request, 'registration/login.html')

def salida(request):
    logout(request)
    return redirect('/')