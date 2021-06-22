from django.shortcuts import render
from .models import Libro

# Create your views here.

def home(request):

    return render(request, 'core/home.html')

def registro(request):

    return render(request, 'core/registro.html')

def libros(request):
    libros=Libro.objects.all()
    datos={
        'libros':libros
    }

    return render(request, 'core/libros.html', datos)