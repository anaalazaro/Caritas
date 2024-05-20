from django import forms

class ChangePasswordForm(forms.Form):
    email = forms.EmailField(label='Correo electrónico')
    current_password = forms.CharField(label='Contraseña actual', widget=forms.PasswordInput)
