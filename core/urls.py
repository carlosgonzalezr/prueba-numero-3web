from django.urls import path
from .views import home, libros, registro

urlpatterns = [
    path('',home,name ="home"),
    path('libros',libros,name ="libros"),
    path('registro',registro,name ="registro"),
]