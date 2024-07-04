from django import forms
from .models import Capitulo

class CapituloForm(forms.ModelForm):
    class Meta:
        model = Capitulo
        fields = ['titulo', 'numero', 'temporada', 'serie', 'descripcion']
        labels = {
            'titulo': 'Título del Capítulo',
            'numero': 'Número del Capítulo',
            'temporada': 'Temporada',
            'serie': 'Serie',
            'descripcion': 'Descripción',
        }

    def clean_numero(self):
        numero = self.cleaned_data.get('numero')
        if numero <= 0:
            raise forms.ValidationError('El número del capítulo debe ser mayor que 0.')
        return numero

    def clean_temporada(self):
        temporada = self.cleaned_data.get('temporada')
        if temporada <= 0:
            raise forms.ValidationError('El número de la temporada debe ser mayor que 0.')
        return temporada