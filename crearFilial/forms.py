from django import forms
from .models import Filial

class FilialForm(forms.ModelForm):
    class Meta:
        model = Filial
        fields = ['nombre']