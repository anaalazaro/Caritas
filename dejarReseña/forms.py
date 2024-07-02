from django import forms
from .models import Reseña

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Reseña
        fields = ['comentario']