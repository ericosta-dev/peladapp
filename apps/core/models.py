from django.db import models

class Configuracoes(models.Model):
    """
    Model de configuração da pelada, podendo configurar informações globais 
    que serão utilizadas em n funcionalidades no sistema.
    """

    nome = models.TextField(max_length=50,verbose_name='Nome da pelada')
    horario = models.TimeField(verbose_name='Horário da pelada')
    mensalidade = models.DecimalField(max_digits=8, decimal_places=2,
                                    verbose_name='Valor por mensalista')
    saldo = models.DecimalField(max_digits=8, decimal_places=2,verbose_name='Saldo em caixa')

    def __str__(self):
        return self.nome

class Pessoa(models.Model):
    """
    Classe que serve de base para outras classes
    """
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15,null=True)
    pix = models.CharField(max_length=100,null=True)

    class Meta:
        abstract = True
