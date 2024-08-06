from django.urls import include
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    path("<str:id>/",views.list_client , name= "list_client")
]
