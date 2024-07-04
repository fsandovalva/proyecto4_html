from django import forms
from .models import Reseña, Serie, Capitulo

class ReseñaForm(forms.ModelForm):
    PUNTUACIONES = [(i / 2, f'{i / 2}') for i in range(0, 11)]  # Opciones de 0 a 5 en incrementos de 0.5

    puntuacion = forms.ChoiceField(choices=PUNTUACIONES)
    serie = forms.ModelChoiceField(queryset=Serie.objects.all(), label='Serie')
    capitulo = forms.ModelChoiceField(queryset=Capitulo.objects.none(), label='Capítulo')
    
    class Meta:
        model = Reseña
        fields = ['titulo', 'serie', 'capitulo', 'contenido', 'puntuacion']
        labels = {
            'titulo': 'Título de la Reseña',
            'serie': 'Serie',
            'capitulo': 'Capítulo',
            'contenido': 'Contenido de la Reseña',
            'puntuacion': 'Puntuación',
        }

    def __init__(self, *args, **kwargs):
        super(ReseñaForm, self).__init__(*args, **kwargs)
        if 'serie' in self.data:
            try:
                serie_id = int(self.data.get('serie'))
                self.fields['capitulo'].queryset = Capitulo.objects.filter(serie_id=serie_id).order_by('numero')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty Capitulo queryset
        elif self.instance.pk:
            self.fields['capitulo'].queryset = self.instance.serie.capitulo_set.order_by('numero')
        
    def clean_puntuacion(self):
        puntuacion = self.cleaned_data.get('puntuacion')
        
        # Convertir el valor a float para asegurar que la comparación numérica sea posible
        try:
            puntuacion = float(puntuacion)
        except ValueError:
            raise forms.ValidationError("La puntuación debe ser un número.")

        if puntuacion < 0 or puntuacion > 5:
            raise forms.ValidationError("La puntuación debe estar entre 0 y 5.")
        
        if puntuacion * 2 != int(puntuacion * 2):
            raise forms.ValidationError("La puntuación debe ser un múltiplo de 0.5.")

        return puntuacion