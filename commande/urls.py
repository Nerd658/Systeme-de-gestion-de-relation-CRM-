from django.urls import include
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    path("",views.list_commande , name= "list_commande"),
    path("ajouter/",views.ajout_commande , name= "ajouter"),
    path("modif/<str:pk>/",views.modif_commande , name= "modif"),
    path("sup/<str:pk>/",views.sup_commande , name= "sup"),
]
 