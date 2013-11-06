__author__ = 'Alex Parra'

from .models import  KeyChain, Servidores, Usuarios
from django.forms import ModelForm, PasswordInput


class KeyChainForm(ModelForm):
    class Meta:
        model = KeyChain
        fields = '__all__'
        widgets = {
            'password': PasswordInput,
        }



