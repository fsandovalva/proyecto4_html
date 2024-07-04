from django.db import models
from django.contrib.auth.models import User
from apps.series.models import Serie, Capitulo
from django.core.validators import MaxValueValidator, MinValueValidator

class Reseña(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    serie = models.ForeignKey(Serie, on_delete=models.CASCADE)
    capitulo = models.ForeignKey(Capitulo, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    puntuacion = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        validators=[
            MaxValueValidator(5.0),
            MinValueValidator(0.0)
        ])

    def __str__(self):
        return self.titulo