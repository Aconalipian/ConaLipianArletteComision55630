from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class f_peliculaForm(forms.Form):
    nombre=forms.CharField(max_length=50, required=True)
    fecha_estreno=forms.DateField(required=True)
    productora=forms.CharField(max_length=50,required=True)
    genero=forms.CharField(max_length=50, required=True)




class f_directorForm(forms.Form):
    nombre=forms.CharField(max_length=50, required=True)
    nacionalidad=forms.CharField(max_length=50, required=True)



class f_productoraForm(forms.Form):
    nombre=forms.CharField(max_length=50, required=True)
    pais=forms.CharField(max_length=50, required=True)




class MiModeloForm(forms.ModelForm):
    class Meta:
        model = cpelicula
        fields = ['nombre','fecha_estreno', 'productora','genero']  
        widgets = {
            'fecha_estreno': forms.DateInput(format='%d-%m-%Y', attrs={'type': 'date'})  # Esto hará que se muestre la barra de fechas
        }

class RegistroUsuariosForm(UserCreationForm):      
    email = forms.EmailField(label="Email de Usuario")
    password1 = forms.CharField(label="Contraseña", widget= forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Contraseña", widget= forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Email de Usuario")
    password1 = forms.CharField(label="Contraseña", widget= forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Contraseña", widget= forms.PasswordInput)
    first_name = forms.CharField(label="nombres",max_length=50, required=False)
    last_name=forms.CharField(label="apellidos",max_length=50, required=False)

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'first_name', 'last_name']

class AvatarFormulario(forms.Form):
    imagen = forms.ImageField(required=True)

