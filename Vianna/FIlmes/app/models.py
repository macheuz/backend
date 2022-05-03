from django.db import models

# Create your models here.
class Filmes(models.Model):
    titulo = models.CharField(max_length=150)
    genero = models.CharField(max_length=100)
    ano = models.IntegerField()