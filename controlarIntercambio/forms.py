from django import forms
from solicitarIntercambio.models import Intercambio
from crearFilial.models import Filial,Turno
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit,Button
    
class RechazarIntercambioForm(forms.ModelForm):
    MOTIVOS = (
        ('motivo1', 'No me gusta'),
        ('motivo2', 'No me conviene'),
        ('motivo3', 'Otro'),
    )

    motivo_rechazo = forms.ChoiceField(choices=MOTIVOS, widget=forms.RadioSelect, label="Motivo de rechazo", required=True)
    class Meta:
        model = Intercambio
        fields = [ 'motivo_rechazo']

    def __init__(self, *args, **kwargs):
        super(RechazarIntercambioForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Fieldset(
                'Rechazar Intercambio',
                'motivo_rechazo',
            ),
            ButtonHolder(
                Submit('accept', 'Rechazar intercambio', css_class='btn btn-primary'),
                Button('cancel', 'Cancelar', css_class='btn btn-secondary', onclick="window.history.back();")
            ),
        )