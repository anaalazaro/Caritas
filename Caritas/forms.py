from django import forms

class CategoriaForm(forms.Form):
    CATEGORIAS_CHOICES = [
        ('ropa', 'Ropa'),
        ('articulos_escolares', 'Artículos Escolares'),
        ('articulos_limpieza', 'Artículos de Limpieza'),
        ('alimentos_noperecederos', 'Alimentos no Perecederos')
    ]
    categoria = forms.ChoiceField(choices=CATEGORIAS_CHOICES, label='Selecciona una categoría')