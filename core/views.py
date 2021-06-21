from django.shortcuts import render
from .models import Libro

# Create your views here.

def home(request):

    return render(request, 'core/home.html')

def registro(request):

    return render(request, 'core/registro.html')

def libros(request):

    return render(request, 'core/libros.html')