from django import forms

class ChangePasswordForm(forms.Form):
    email = forms.EmailField(label='Correo electrónico')
