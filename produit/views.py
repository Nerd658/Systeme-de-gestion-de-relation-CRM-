from django.shortcuts import render
from django.http import HttpResponse
from client.models import Client
from commande.models import Commande

from django.contrib.auth.decorators import login_required

@login_required(login_url="connexion")
def acceuil (request) :
    commandes = Commande.objects.all()
    clients = Client.objects.all()
    context = {
        "clients" : clients,
        "commandes" : commandes,
    }
    return render (request , "produit/acceuil.html", context)