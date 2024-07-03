from django import forms
from solicitarIntercambio.models import Intercambio
from crearFilial.models import Filial,Turno
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit,Button
    
class RechazarIntercambioForm(forms.Form):
    MOTIVOS = (
        ('No me gusta', 'No me gusta'),
        ('No me conviene', 'No me conviene'),
        ('Prefiero otro intercambio', 'Prefiero otro intercambio'),
        ('No me interesa', 'No me interesa'),
        ('Otro', 'Otro'),
    )

    # otro_motivo = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'otro_motivo'}),label='Indique otro motivo:')
    motivo_rechazo = forms.ChoiceField(choices=MOTIVOS, widget=forms.RadioSelect(attrs={'onchange': 'clearInputsAndSubmit(this);'}), label="Motivo de rechazo:", required=True)
    otro_motivo = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'otro_motivo', 'style': 'display:none;', 'placeholder': 'Por favor, indique el motivo','maxlength': '40'}),label='', required=False)
