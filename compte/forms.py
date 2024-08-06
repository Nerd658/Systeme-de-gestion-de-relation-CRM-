from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from .models import CompteModel
from django import forms

class CompteForm(UserCreationForm) :
    class Meta :
        model = User
        fields =[
            "username" ,
            "password1", 
            "password2" ,
        ]

# class CompteAuth(forms.Form) :
#     username = forms.CharField(max_length=25)
#     password = forms.CharField(widget=forms.PasswordInput)
#     class Meta :
#         fields = [
#             "username",
#             "password",
#         ]