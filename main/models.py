from django.db import models
from django.contrib.auth.models import User

class Caracteristicas(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    idade = models.PositiveIntegerField(default=None)
    peso_inicial = models.FloatField(default=None)
    peso_atual = models.FloatField(default=None)
    altura =  models.FloatField(default=None)
    inicio = models.DateField(auto_now_add=True)


class Metas(models.Model):

    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    peso = models.FloatField(default=None)
    calorias = models.PositiveIntegerField(default=None)

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
  
    agua = models.FloatField(default=None, choices=AGUA)

class PesoHistory(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    peso = models.FloatField(default=None)
    created = models.DateField(auto_now_add=True)

class Ingestao(models.Model):
    agua = models.PositiveIntegerField(default=None)
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created = models.DateField(auto_now_add=True)

    @property
    def get_day(self):
        return self.created.day
    
    def get_month(self):
        return self.created.month

    