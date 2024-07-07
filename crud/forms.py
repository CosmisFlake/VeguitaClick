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
            'peso',
            'tipo_peso',
            'stock',
            'image'
        ]
        labels = {
            'idProducto':'ID',
            'name':'Nombre',
            'proveedor':'Proveedor',
            'tipo':'Tipo de Producto',
            'value':'Valor',
            'peso':'Peso',
            'tipo_peso':'Tipo de Peso',
            'stock':'Stock',
            'image':'Imagen'
        }
        widgets = {
            'idProducto':forms.TextInput(attrs={'class':'form-control'}),
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'tipo':forms.Select(attrs={'class':'form-control'}),
            'proveedor':forms.Select(attrs={'class':'form-control'}),
            'value':forms.TextInput(attrs={'class':'form-control','type':'number'}),
            'peso':forms.TextInput(attrs={'class':'form-control','type':'number'}),
            'tipo_peso':forms.Select(attrs={'class':'form-control'}),
            'stock':forms.TextInput(attrs={'class':'form-control','type':'number'}),
            'image':forms.FileInput(attrs={'class':'form-control'})
        }

class ProveedorForm(ModelForm):
    class Meta:
        model = Proveedor
        fields = [
            'id',
            'proveedor',
            'direccion',
            'rut'
        ]
        labels = {
            'id':'ID',
            'proveedor':'Nombre de proveedor',
            'direccion':'Direccion de proveedor',
            'rut':'Rut de proveedor'

        }
        widgets = {
            'id':forms.TextInput(attrs={'class':'form-control'}),
            'proveedor':forms.TextInput(attrs={'class':'form-control'}),
            'direccion':forms.TextInput(attrs={'class':'form-control'}),
            'rut':forms.TextInput(attrs={'class':'form-control'})
        }

class TipoProductoForm(ModelForm):
    class Meta:
        model = TipoProducto
        fields = [
            'id',
            'tipo'
        ]
        labels = {
            'id':'ID',
            'tipo':'Tipo de producto'
        }
        widgets = {
            'id':forms.TextInput(attrs={'class':'form-control'}),
            'tipo':forms.TextInput(attrs={'class':'form-control'})
        }

class TipoPesoForm(ModelForm):
    class Meta:
        model = TipoPeso
        fields = [
            'id',
            'tipo_peso'
        ]
        labels = {
            'id':'ID',
            'tipo_peso':'Tipo de peso'
        }
        widgets = {
            'id':forms.TextInput(attrs={'class':'form-control'}),
            'tipo_peso':forms.TextInput(attrs={'class':'form-control'})
        }

class TipoVehiculoForm(ModelForm):
    class Meta:
        model = TipoVehiculo
        fields = [
            'id',
            'tipo'
        ]
        labels = {
            'id':'ID',
            'tipo':'Tipo de vehiculo'
        }
        widgets = {
            'id':forms.TextInput(attrs={'class':'form-control'}),
            'tipo':forms.TextInput(attrs={'class':'form-control'})
        }

class EstadoVehiculoForm(ModelForm):
    class Meta:
        model = EstadoVehiculo
        fields = [
            'id',
            'estado'
        ]
        labels = {
            'id':'ID',
            'estado':'Estado de vehiculo'
        }
        widgets = {
            'id':forms.TextInput(attrs={'class':'form-control'}),
            'estado':forms.TextInput(attrs={'class':'form-control'})
        }

class VehiculoForm(ModelForm):
    class Meta:
        model = Vehiculo
        fields = [
            'idVehiculo',
            'nombre',
            'tipo',
            'color',
            'estado',
            'image'
        ]
        labels = {
            'idVehiculo':'ID',
            'nombre':'Nombre',
            'tipo':'Tipo de Vehiculo',
            'color':'Color del Vehiculo',
            'estado':'Estado del Vehiculo',
            'image':'Imagen'
        }
        widgets = {
            'idVehiculo':forms.TextInput(attrs={'class':'form-control'}),
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'tipo':forms.Select(attrs={'class':'form-control'}),
            'color':forms.TextInput(attrs={'class':'form-control'}),
            'estado':forms.Select(attrs={'class':'form-control'}),
            'image':forms.FileInput(attrs={'class':'form-control'})
        }

class TransportistaForm(ModelForm):
    class Meta:
        model = Transportista
        fields = [
            'id',
            'nombre',
            'direccion',
            'rut',
            'image'
        ]
        labels = {
            'id':'ID',
            'nombre':'Nombre',
            'direccion':'Direccion',
            'rut':'Rut',
            'image':'Imagen'
        }
        widgets = {
            'id':forms.TextInput(attrs={'class':'form-control'}),
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'direccion':forms.TextInput(attrs={'class':'form-control'}),
            'rut':forms.TextInput(attrs={'class':'form-control'}),
            'image':forms.FileInput(attrs={'class':'form-control'})
        }

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = [
            'id',
            'nombre',
            'direccion',
            'rut',
            'email'
        ]
        labels = {
            'id':'ID',
            'nombre':'Nombre',
            'direccion':'Direccion',
            'rut':'Rut',
            'email':'Email'
        }
        widgets = {
            'id':forms.TextInput(attrs={'class':'form-control'}),
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'direccion':forms.TextInput(attrs={'class':'form-control'}),
            'rut':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'})
        }