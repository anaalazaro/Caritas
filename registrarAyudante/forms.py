from django import forms
from . models import CustomUser
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext, gettext_lazy as _
from datetime import datetime
from django.core.exceptions import ValidationError


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = [
            'dni',
            'password1',
            'password2',
            'telefono',
            'fecha_nacimiento',
            'filial',
            #'roles'
        ]
        labels = {
            'dni': _('DNI'),
            'password1': _('Contraseña'),
            'password2': _('Repetir contraseña'),
            'telefono': _('Teléfono'),
            'fecha_nacimiento': _('Fecha de nacimiento'),
            'filial': _('Filial'),
            #'roles': _('Rol del usuario'),
        }
    fecha_nacimiento = forms.DateField(
        label=_('Fecha de nacimiento'),
        widget=forms.DateInput(attrs={'type': 'date'}),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Modificar los mensajes de validación de la contraseña
        self.fields['password1'].help_text = _("La contraseña debe tener al menos 8 caracteres y ser alfanumérica.")
        self.fields['password2'].help_text = _("Repetir contraseña")

    def clean_dni(self):
        dni = self.cleaned_data.get('dni')
        if CustomUser.objects.filter(dni=dni).exists():
           raise forms.ValidationError(_("Este DNI ya está registrado. Por favor, utiliza otro."))
        return dni

    def clean_fecha_nacimiento(self):
        fecha_nacimiento = self.cleaned_data.get('fecha_nacimiento')
        today = datetime.today()
        age = today.year - fecha_nacimiento.year - ((today.month, today.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
        if age < 18:
            raise forms.ValidationError(_("Debe tener al menos 18 años para registrarse."))
        return fecha_nacimiento

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if len(password1) < 8:
            raise forms.ValidationError(_("La contraseña debe tener al menos 8 caracteres."))
        if not password1.isalnum():
            raise forms.ValidationError(_("La contraseña debe ser alfanumérica."))
        return password1
    
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(_("Las contraseñas no coinciden."))
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['dni']  # Establecer el nombre de usuario como el DNI
        user.roles = 'ayudante'  # Establecer el nombre de usuario como el DNI
        if commit:
            user.save()
        return user