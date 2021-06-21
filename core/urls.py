from django.urls import path
from .views import home

url = [
    path('',home,name ="home"),
]