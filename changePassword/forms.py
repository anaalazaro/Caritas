from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.password_validation import validate_password
from django.utils.translation import gettext as _


class DesiredPasswordChangeForm(PasswordChangeForm):
    new_password1 = forms.CharField(
        label=_("New password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text=_("Su contraseña debe contener al menos 6 caracteres, y debe incluir letras y números"),
    )

    def __init__(self, user, *args, **kwargs):
        super().__init__(user, *args, **kwargs)
        self.fields['old_password'].label = _("Ingrese la contraseña autogenerada que recibió por correo electrónico")
        self.fields['new_password1'].label = _("Ingrese la nueva contraseña")
        self.fields['new_password2'].label = _("Ingrese nuevamente la nueva contraseña")

    def clean_new_password1(self):
        password = self.cleaned_data.get('new_password1')
        if len(password) < 6:
            raise forms.ValidationError(_("The new password must be at least 6 characters long."))
        if not any(char.isdigit() for char in password) or not any(char.isalpha() for char in password):
            raise forms.ValidationError(_("The new password must contain both letters and numbers."))
        validate_password(password)  # Django's built-in password validation
        return password