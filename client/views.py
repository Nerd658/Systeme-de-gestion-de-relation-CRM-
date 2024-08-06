from django.shortcuts import render
from .models import Client
from .filters import CommandFilter
# Create your views here.

from django.http import HttpResponse
def list_client (request, id) :
    
    client = Client.objects.get(pk = id)
    commandes = client.commande_set.all()
    commandes_all = commandes.count()
    
    myfilter = CommandFilter(request.GET,queryset=commandes)
    commandes = myfilter.qs
    
    return render(request, "client/list_client.html", 
        context= {
        "client" : client,
        "commandes" : commandes,
        "commandes_all" : commandes_all,
        "myfilter" :myfilter
        
    })
    
