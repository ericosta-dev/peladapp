from django.db import models
from core.models import Pessoa

# Create your models here.
class Pelada(models.Model):
    data = models.DateField(verbose_name='Data de realização')