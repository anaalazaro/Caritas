from django import forms
from .models import Articulo

class ArticuloForm(forms.ModelForm):
    CATEGORIAS_CHOICES = [
        ('Ropa', 'Ropa'),
        ('Articulos Escolares', 'Artículos Escolares'),
        ('Articulos De Limpieza', 'Artículos de Limpieza'),
        ('Alimentos No Perecederos', 'Alimentos No Perecederos'),
    ]

    Categoria = forms.ChoiceField(choices=CATEGORIAS_CHOICES)

    class Meta:
        model = Articulo
        fields = ['Foto', 'Categoria', 'Titulo', 'Descripcion', 'Estado']
