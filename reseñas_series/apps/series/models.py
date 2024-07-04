from django.db import models

class Serie(models.Model):
    titulo = models.CharField(max_length=200)
    sinopsis = models.TextField()
    imagen = models.ImageField(upload_to='series/', blank=True, null=True)


    def __str__(self):
        return self.titulo

class Capitulo(models.Model):
    titulo = models.CharField(max_length=200)
    numero = models.IntegerField()  # Número del capítulo dentro de la temporada
    temporada = models.IntegerField()  # Número de la temporada
    serie = models.ForeignKey(Serie, on_delete=models.CASCADE, related_name='capitulos')
    descripcion = models.TextField()

    def __str__(self):
        return f"{self.titulo} (Temporada {self.temporada}, Episodio {self.numero})"