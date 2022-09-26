from django.db import models
from django.contrib.auth.models import User

class Caracteristicas(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    idade = models.IntegerField(default=0)
    peso_inicial = models.FloatField(default=0)
    peso_atual = models.FloatField(default=0)
    altura =  models.FloatField(default=0)
    inicio = models.DateField(auto_now_add=True)


class Metas(models.Model):

    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    peso = models.FloatField(default=0)
    calorias = models.IntegerField(default=0)

    um = 1
    um_meio = 1.5
    dois = 2
    dois_meio = 2.5
    tres = 3

    AGUA = (
    (um, '1 litro'),
    (um_meio, '1.5 litros'),
    (dois, '2 litros'),
    (dois_meio, '2.5 litros'),
    (tres, '3 litros'),
    )
  
    agua = models.FloatField(default=0, choices=AGUA)

class PesoHistory(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    peso = models.FloatField(default=0)
    created = models.DateField(auto_now_add=True)