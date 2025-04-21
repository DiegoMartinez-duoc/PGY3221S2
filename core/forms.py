from django import forms
from .models import ThreadUser, CredencialesUsuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = ThreadUser
        fields = ['nombre', 'nombre_usuario', 'fecha_nacimiento']


class CredencialesForm(forms.ModelForm):
    class Meta:
        model = CredencialesUsuario
        fields = ['email', 'contrasena', 'rol']
        