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
    Classe abstrata que representa uma pessoa, que pode ser um jogador ou goleiro.
    Possui os seguintes atributos:

    Atributos:
        nome (str): Nome completo da pessoa.
        telefone (str, opcional): Número de telefone da pessoa.
        pix (str, opcional): Chave Pix da pessoa.

    """
    nome = models.CharField(max_length=100,verbose_name='Nome')
    telefone = models.CharField(max_length=15,null=True,verbose_name='Telefone')
    pix = models.CharField(max_length=100,null=True,verbose_name='Chave Pix')

    class Meta:
        abstract = True

class Jogador(Pessoa):
    """
    Representa um jogador, que é um integrante da pelada que joga na linha. 
    Herda da classe Pessoa e adiciona um campo para o tipo de jogador (avulso ou mensalista).
    Possui os seguintes atributos:

    Atributos:
        nome (str): Nome do jogador.
        telefone (str, opcional): Telefone do jogador.
        pix (str, opcional): Chave Pix do jogador.
        tipo (int): Tipo de jogador, que pode ser 1 (avulso) ou 2 (mensalista).

    """

    AVULSO = 1
    MENSALISTA = 2
    TIPOS_PESSOA_CHOICES = (
        (AVULSO, 'Avulso'),
        (MENSALISTA, 'Mensalista'),
    )

    tipo = models.IntegerField(default=1,choices=TIPOS_PESSOA_CHOICES,verbose_name='Tipo')

    def __str__(self):
            return self.nome
