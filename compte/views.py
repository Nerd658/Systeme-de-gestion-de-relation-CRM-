from django.shortcuts import render , redirect

from .forms import CompteForm
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib import messages

# Create your views here.
def inscription (request) :
    form = CompteForm(request.POST)
    if request.method == "POST" :
        form = CompteForm(request.POST)
        if form.is_valid() :
            form.save()
            return redirect ("connexion")
        else:
            messages.error(request, "Veuillez corriger les erreurs ci-dessous.")
    else :
        form = CompteForm()
    return render(request , 'compte/inscription.html' ,
                  context= {
                      "form" : form
                  })

def connexion (request) :
    if request.method == "POST" :
        username = request.POST["username"]
        password = request.POST["password"]
        
        user = authenticate(User , username=username , password=password)
        if user is not None :
            login(request, user)
            return redirect("acceuil")
        else : 
            messages.error(request, "le mot de passe ou l'username est incorect")
            
    
    return render(request , 'compte/connexion.html' )

from django.contrib.auth import logout
def deconnexion (request) :
    logout(request)
    return redirect("connexion")