from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from datetime import datetime
from django.core.exceptions import ValidationError
from django.utils.translation import gettext, gettext_lazy as _


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ['nombre', 'apellido', 'mail', 'dni', 'password1', 'telefono', 'fechaNacimiento']
        labels = {
            'nombre':_('Nombre'),
            'apellido':_('Apellido'),
            'mail':_('Mail'),
            'telefono': _('Teléfono'),
            'dni': _('DNI'),
            'fechaNacimiento': _('Fecha de nacimiento'),
            'password1': _('Contraseña'),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].required = True
        self.fields['apellido'].required = True
        self.fields['mail'].required=True


    fechaNacimiento = forms.DateField(
        label=_('Fecha de nacimiento'),
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Modificar los mensajes de validación de la contraseña
        self.fields['password1'].help_text = _("La contraseña debe poseer 6 o más caracteres")
        # Agregar clases CSS al formulario
        self.fields['dni'].widget.attrs.update({'class': 'form-control'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['telefono'].widget.attrs.update({'class': 'form-control'})

    def clean_dni(self):
        dni = self.cleaned_data.get('dni')
        if CustomUser.objects.filter(dni=dni).exists():
            raise forms.ValidationError(_("Ya existe un usuario registrado con ese número de DNI"))
        return dni

    def clean_fechaNacimiento(self):
        fecha_nacimiento = self.cleaned_data.get('fechaNacimiento')
        today = datetime.today()
        age = today.year - fecha_nacimiento.year - ((today.month, today.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
        if age < 18:
            raise forms.ValidationError(_("No puedes registrarte en el sistema por ser menor de edad"))
        return fecha_nacimiento

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if len(password1) < 6:
            raise forms.ValidationError(_("La contraseña debe poseer 6 o más caracteres"))
        if not password1.isalnum():
            raise forms.ValidationError(_("La contraseña debe ser alfanumérica."))
        return password1

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['dni']  # Establecer el nombre de usuario como el DNI
        user.roles= 'usuario'
        if commit:
            user.save()
        return user
