from django import forms
from django.forms import ModelForm
from .models import *

class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = [
            'idProducto',
            'name',
            'proveedor',
            'tipo',
            'value',
            'stock',
            'image'
        ]
        labels = {
            'idProducto':'ID',
            'name':'Nombre',
            'proveedor':'Proveedor',
            'tipo':'Tipo de Producto',
            'value':'Valor',
            'stock':'Stock',
            'image':'Imagen'
        }
        widgets = {
            'idProducto':forms.TextInput(attrs={'class':'form-control'}),
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'tipo':forms.TextInput(attrs={'class':'form-control'}),
            'proveedor':forms.Select(attrs={'class':'form-control'}),
            'value':forms.TextInput(attrs={'class':'form-control','type':'number'}),
            'stock':forms.TextInput(attrs={'class':'form-control','type':'number'}),
            'image':forms.FileInput(attrs={'class':'form-control'})
        }

class ProveedorForm(ModelForm):
    pass