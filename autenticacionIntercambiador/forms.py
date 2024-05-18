from django import forms

class LoginForm(forms.Form):
    dni = forms.CharField(max_length=10, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True,  label="Contraseña")