from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from datetime import datetime
from django.core.exceptions import ValidationError
from django.utils.translation import gettext, gettext_lazy as _


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ['dni', 'password1', 'telefono', 'fechaNacimiento']
        labels = {
            'dni': _('DNI'),
            'password1': _('Contraseña'),
            'telefono': _('Teléfono'),
            'fechaNacimiento': _('Fecha de nacimiento'),
        }

    fechaNacimiento = forms.DateField(
        label=_('Fecha de nacimiento'),
        widget=forms.DateInput(attrs={'type': 'date'}),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Modificar los mensajes de validación de la contraseña
        self.fields['password1'].help_text = _("La contraseña debe tener al menos 6 caracteres y ser alfanumérica.")

    def clean_dni(self):
        dni = self.cleaned_data.get('dni')
        if CustomUser.objects.filter(dni=dni).exists():
            raise forms.ValidationError(_("Este DNI ya está registrado. Por favor, utiliza otro."))
        return dni

    def clean_fechaNacimiento(self):
        fecha_nacimiento = self.cleaned_data.get('fechaNacimiento')
        today = datetime.today()
        age = today.year - fecha_nacimiento.year - ((today.month, today.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
        if age < 18:
            raise forms.ValidationError(_("Debe tener al menos 18 años para registrarse."))
        return fecha_nacimiento

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if len(password1) < 6:
            raise forms.ValidationError(_("La contraseña debe tener al menos 6 caracteres."))
        if not password1.isalnum():
            raise forms.ValidationError(_("La contraseña debe ser alfanumérica."))
        return password1

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['dni']  # Establecer el nombre de usuario como el DNI
        if commit:
            user.save()
        return user
