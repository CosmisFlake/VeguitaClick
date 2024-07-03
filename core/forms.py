from django import forms
from django.forms import ModelForm
from .models import *

class ProductForm(ModelForm):
    
    class Meta:
        model = Product
        fields = [
            'name',
            'email',
            'address',
            'city',
            'rut',
            'tipo_envio'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dirección'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Comuna'}),
            'rut': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Rut'}),
            'tipo_envio': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Tipo de Envio'})
        }