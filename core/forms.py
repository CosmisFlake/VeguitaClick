from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class CreateUserForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Correo'}))
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
def __init__(self, *args, **kwargs):
	super(CreateUserForm, self).__init__(*args, **kwargs)
	self.fields['username'].widget.attrs['class'] = 'form-control'
	self.fields['username'].widget.attrs['placeholder'] = 'Nombre de Usuario'
	self.fields['username'].label = ''
	self.fields['username'].help_text = '<span class="form-text text-muted"><small>Requerido. 150 caracteres o menos. Letras, digitos y solo @/./+/-/_.</small></span>'

	self.fields['password1'].widget.attrs['class'] = 'form-control'
	self.fields['password1'].widget.attrs['placeholder'] = 'Contraseña'
	self.fields['password1'].label = ''
	self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Tu contraseña no puede ser similar a tu otra informacion personal.</li><li>Tu contraseña debe tener al menos 8 caracteres.</li><li>Tu contraseña no puede ser una usada comumente.</li><li>Tu contraseña no puede ser enteramente numerica.</li></ul>'

	self.fields['password2'].widget.attrs['class'] = 'form-control'
	self.fields['password2'].widget.attrs['placeholder'] = 'Confirmar Contraseña'
	self.fields['password2'].label = ''
	self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Ingresa la misma contraseña como antes, para verificacion.</small></span>'    
   