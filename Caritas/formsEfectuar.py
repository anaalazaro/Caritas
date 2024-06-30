from django import forms

class OpcionesCodigos(forms.Form):
    OPCIONES = [
        ('opcion1', 'Ingresar códigos del solicitante y destinatario.'),
        ('opcion2', 'Ingresar código del solicitante.'),
        ('opcion3', 'Ingresar código del destinatario.'),
    ]

    seleccion = forms.ChoiceField(choices=OPCIONES, widget=forms.RadioSelect(attrs={'onchange': 'this.form.submit();', 'class': 'form-check-inline'}),required=True)