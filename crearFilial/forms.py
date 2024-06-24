from django import forms
from .models import Filial

class FilialForm(forms.ModelForm):
    class Meta:
        model = Filial
        fields = ['nombre', 'latitud', 'longitud']
        widgets = {
            'latitud': forms.HiddenInput(),
            'longitud': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['latitud'].widget.attrs['id'] = 'id_latitud'
        self.fields['longitud'].widget.attrs['id'] = 'id_longitud'
        