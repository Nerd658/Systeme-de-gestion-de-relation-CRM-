from django.urls import include
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    path("",views.acceuil , name= "acceuil")
]
