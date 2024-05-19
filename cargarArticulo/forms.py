from django import forms
from .models import Articulo

class ArticuloForm(forms.ModelForm):
    def __init__(self, *args, usuario=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.usuario = usuario

    class Meta:
        model = Articulo
        fields = ['Foto', 'Categoria', 'Titulo', 'Descripcion', 'Estado']

    def save(self, commit=True):
        instancia = super().save(commit=False)
        instancia.usuario = self.usuario
        if commit:
            instancia.save()
        return instancia
