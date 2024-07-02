from django import forms
from app.models import CustomUser
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext, gettext_lazy as _
from datetime import datetime
from django.core.exceptions import ValidationError
from django.contrib.auth import password_validation


class CustomUserCreationForm(UserCreationForm):
    
    fechaNacimiento = forms.DateField(
        label=_('Fecha de nacimiento'),
        widget=forms.DateInput(attrs={'type': 'date'})
    )

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
            'nombre',
            'apellido',
            'mail',
            'password1',
            'password2',
            'telefono',
            'fechaNacimiento',
        ]
        labels = {
            'dni': _('DNI'),
            'nombre':_('Nombre'),
            'apellido':_('Apellido'),
            'mail': _('Email'),
            'password1': _('Contraseña'),
            'password2': _('Repetir contraseña'),
            'telefono': _('Teléfono'),
            'fechaNacimiento': _('Fecha de nacimiento'),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = _("La contraseña debe tener al menos 6 caracteres y ser alfanumérica.")
        self.fields['password2'].help_text = _("Ingrese la misma contraseña que antes, para verificarla")

    def clean_dni(self):
        dni = self.cleaned_data.get('dni')
        existing_user = CustomUser.objects.filter(dni=dni).first()
        
        if existing_user:
            if existing_user.borrado:
                # Permitir registro si el usuario existe pero está marcado como borrado
                return dni
            else:
                # Usuario activo con el mismo DNI
                raise forms.ValidationError(_("Este DNI ya está registrado. Por favor, utiliza otro."))
        
        return dni

    def clean_fechaNacimiento(self):
        fechaNacimiento = self.cleaned_data.get('fechaNacimiento')
        today = datetime.today()
        age = today.year - fechaNacimiento.year - ((today.month, today.day) < (fechaNacimiento.month, fechaNacimiento.day))
        if age < 18:
            raise forms.ValidationError(_("Debe tener al menos 18 años para registrarse."))
        return fechaNacimiento

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        
        if len(password1) < 6:
            raise forms.ValidationError(_("La contraseña debe poseer 6 o más caracteres"))
        
        if password1.isalnum():
            has_letter = any(char.isalpha() for char in password1)
            has_number = any(char.isdigit() for char in password1)
            
            if not (has_letter and has_number):
                raise forms.ValidationError(_("La contraseña debe ser alfanumérica"))
        else:
            raise forms.ValidationError(_("La contraseña debe ser alfanumérica"))
        
        return password1
    
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password1 != password2:
            raise forms.ValidationError(_("Las contraseñas no coinciden."))
        if len(password2) < 6:
            raise forms.ValidationError(_('La contraseña debe tener al menos 6 caracteres.'))
        return password2

    def clean_telefono(self):
        telefono = self.cleaned_data['telefono']
        if not telefono.startswith('221'):
            raise ValidationError('El teléfono debe corresponder a La Plata')
        return telefono

    def clean_mail(self):
        email = self.cleaned_data.get('mail')
        if CustomUser.objects.filter(mail=email).exists():
            raise ValidationError('Ya existe un usuario con este correo electrónico.')
        return email
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['dni']  # Establecer el nombre de usuario como el DNI
        user.roles = 'usuario' 
        if commit:
            user.save()
        return user
