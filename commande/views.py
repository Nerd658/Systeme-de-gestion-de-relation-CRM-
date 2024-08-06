from django.shortcuts import render , redirect
from django.http import HttpResponse
# Create your views here.
from .forms import ModelForm , CommandForm

from .models import Commande





def list_commande (request) :
    return render(request, "commande/list_commande.html")

def ajout_commande (request) :
    form = CommandForm()
    if request.method == "POST" :
        form = CommandForm(request.POST)
        if form.is_valid () :
            form.save()
            return redirect ("acceuil")
        
    context= {
        "form" : form
    }
    
    return render(request, "commande/ajout_commande.html" , context )



def modif_commande (request , pk) :
    commande = Commande.objects.get( id = pk)
    form = CommandForm( instance=commande)
    if request.method == "POST" :
        form = CommandForm(request.POST , instance=commande)
        if form.is_valid () :
            form.save()
            return redirect ("acceuil")
        
    context= {
        "form" : form
    }
    
    return render(request, "commande/ajout_commande.html" , context )


def sup_commande (request , pk) :
    commande = Commande.objects.get( id = pk)
    
    if request.method == "POST" :
        commande.delete()
        return redirect("acceuil")
        
        
    context= {
        "commande" : commande
    }
    
    return render(request, "commande/sup_commande.html" , context )


