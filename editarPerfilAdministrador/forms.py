from django import forms
from registrarAyudante.models import CustomUser
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.utils.translation import gettext, gettext_lazy as _

class UsuarioIntercambiadorForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name','last_name']
        labels = {
            'first_name': _('Nombre'),
            'last_name': _('Apellido'),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'