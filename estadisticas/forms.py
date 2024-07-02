from django import forms
from crearFilial.models import Filial
from django.core.exceptions import ValidationError

class DateRangeForm(forms.Form):
    fecha_desde = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}),label='Fecha desde:*')
    fecha_hasta = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}),label='Fecha hasta:*')
    filial = forms.ModelChoiceField(queryset=Filial.objects.all(), required=True, label="Seleccione una filial:*")

    def clean(self):
        cleaned_data = super().clean()
        fecha_desde = cleaned_data.get('fecha_desde')
        fecha_hasta = cleaned_data.get('fecha_hasta')

        if fecha_desde and fecha_hasta and fecha_desde > fecha_hasta:
            raise ValidationError("La fecha hasta debe ser mayor que la fecha desde.")
        return cleaned_data
    
class FilialForm(forms.Form):
    filial = forms.ModelChoiceField(queryset=Filial.objects.all(), required=True, label="Seleccione una filial:*")