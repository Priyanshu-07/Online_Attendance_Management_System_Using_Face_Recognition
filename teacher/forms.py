from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django import forms

class Userloginform(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(Userloginform, self).__init__(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'input', 'type':'text', 'placeholder': 'enter username' 
        }))
    password = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'input', 'type':'password', 'placeholder': 'enter password' 
        }))