from django import forms
from solicitarIntercambio.models import Intercambio
from crearFilial.models import Filial,Turno
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
    
class RechazarIntercambioForm(forms.ModelForm):
    motivo_rechazo = forms.CharField(widget=forms.Textarea, label="Motivo de rechazo", required=False)

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
                Submit('accept', 'Rechazar intercambio', css_class='btn btn-primary')
            ),
        )