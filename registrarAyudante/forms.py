from django import forms
from . models import CustomUser
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext, gettext_lazy as _
from datetime import datetime
from django.core.exceptions import ValidationError
# from django.core.validators import EmailValidator
# import re
from django.contrib.auth import password_validation


class CustomUserCreationForm(UserCreationForm):
    
    fecha_nacimiento = forms.DateField(
        label=_('Fecha de nacimiento'),
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    # email = forms.EmailField(
    #     validators=[EmailValidator()],
    #     error_messages={
    #         'invalid': 'Introduce una dirección de correo electrónico válida.',
    #     }
    # )
    # email = forms.EmailField(label=_("Email"), required=True)
    last_name = forms.CharField(label=_("Apellido"), required=True)
    first_name = forms.CharField(label=_("Nombre"), required=True)
    password1 = forms.CharField(
        label=_("Contraseña"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Repetir contraseña"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = [
            'dni',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
            'telefono',
            'fecha_nacimiento',
            'filial',
            #'roles'
        ]
        labels = {
            'dni': _('DNI'),
            'first_name': _('Nombre'),
            'last_name':_('Apellido'),
            'email': _('Email'),
            'password1': _('Contraseña'),
            'password2': _('Repetir contraseña'),
            'telefono': _('Teléfono'),
            'fecha_nacimiento': _('Fecha de nacimiento'),
            'filial': _('Filial'),
            #'roles': _('Rol del usuario'),
        }



    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Modificar los mensajes de validación de la contraseña
        self.fields['password1'].help_text = _("La contraseña debe tener al menos 6 caracteres y ser alfanumérica.")
        self.fields['password2'].help_text = _("Ingrese la misma contraseña que antes, para verificarla")

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
        if len(password1) < 6:
            raise forms.ValidationError(_("La contraseña debe tener al menos 6 caracteres."))
        if not password1.isalnum():
            raise forms.ValidationError(_("La contraseña debe ser alfanumérica."))
        return password1
    
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1  and password1 != password2:
            raise forms.ValidationError(_("Las contraseñas no coinciden."))
        if len(password2) < 6:
            raise forms.ValidationError(_('La contraseña debe tener al menos 6 caracteres.'))
        return password2

    def clean_telefono(self):
        telefono = self.cleaned_data['telefono']
        if not telefono.startswith('221'):
            raise ValidationError('El teléfono debe corresponder a La Plata')
        return telefono

    # def clean_email(self):
    #     email = self.cleaned_data.get('email')
    #     # if CustomUser.objects.filter(email=email).exists():
    #     #     raise ValidationError('Ya existe un usuario con este correo electrónico.')
    #     if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
    #         raise ValidationError(_('El formato del correo electrónico es incorrecto.'))
    #     return email
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['dni']  # Establecer el nombre de usuario como el DNI
        user.roles = 'ayudante'  # Establecer el nombre de usuario como el DNI
        if commit:
            user.save()
        return user