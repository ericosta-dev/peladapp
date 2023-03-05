from django.db import models

from apps.core.models import Goleiro, Jogador

# Create your models here.
class Pelada(models.Model):
    data = models.DateField(verbose_name="Data de realização")
    saldo = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)


class PresencaJogador(models.Model):
    jogador = models.ForeignKey(Jogador, on_delete=models.CASCADE)
    pelada = models.ForeignKey(Pelada, on_delete=models.CASCADE)
    vl_pago = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)


class PresencaGoleiro(models.Model):
    goleiro = models.ForeignKey(Goleiro, on_delete=models.CASCADE)
    pelada = models.ForeignKey(Pelada, on_delete=models.CASCADE)
    vl_pago = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
