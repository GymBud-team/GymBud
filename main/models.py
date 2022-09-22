from django.db import models
from django.contrib.auth.models import User

class Metas(models.Model):

    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    peso = models.IntegerField(default=0)
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
  

    agua = models.IntegerField(default=0, choices=AGUA)
