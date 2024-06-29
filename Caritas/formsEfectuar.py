from django import forms

class OpcionesCodigos(forms.Form):
    OPCIONES = [
        ('opcion1', 'Ingresar códigos del solicitante y destinatario.'),
        ('opcion2', 'Ingresar código del solicitante.'),
        ('opcion3', 'Ingresar código del destinatario.'),
    ]

    seleccion = forms.ChoiceField(choices=OPCIONES, widget=forms.RadioSelect(attrs={'onchange': 'clearInputsAndSubmit(this);'}),required=True)
    codigo_solicitante = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'codigo_solicitante'}))
    codigo_destinatario = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'codigo_destinatario'}))