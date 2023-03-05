from django.db import models


class Configuracoes(models.Model):
    """
    Model que armazena as configurações da pelada, incluindo o nome da pelada, o horário em que ela ocorre, a mensalidade
    para jogadores mensalistas e o saldo em caixa. Possui os seguintes atributos:

    Atributos:
        nome (str): Nome da pelada.
        horario (Time): Horário em que a pelada ocorre.
        mensalidade (Decimal): Valor da mensalidade para jogadores mensalistas.
        saldo (Decimal): Saldo em caixa da pelada.

    Métodos:
        __str__(): Retorna o nome da pelada como uma string.

    """

    nome = models.TextField(max_length=50, verbose_name="Nome da pelada")
    horario = models.TimeField(verbose_name="Horário da pelada")
    vl_mensalidade = models.DecimalField(
        max_digits=8, decimal_places=2, verbose_name="Valor por mensalista"
    )
    vl_avulso = models.DecimalField(
        max_digits=8, decimal_places=2, verbose_name="Valor por avulso"
    )
    saldo = models.DecimalField(
        max_digits=8, decimal_places=2, verbose_name="Saldo em caixa"
    )

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Configuração"
        verbose_name_plural = "Configurações"


class Pessoa(models.Model):
    """
    Classe abstrata que representa uma pessoa, que pode ser um jogador ou goleiro.
    Possui os seguintes atributos:

    Atributos:
        nome (str): Nome completo da pessoa.
        telefone (str, opcional): Número de telefone da pessoa.
        pix (str, opcional): Chave Pix da pessoa.

    """

    nome = models.CharField(max_length=100, verbose_name="Nome")
    telefone = models.CharField(
        max_length=15, null=True, verbose_name="Telefone", blank=True
    )
    pix = models.CharField(
        max_length=100, null=True, verbose_name="Chave Pix", blank=True
    )

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

    Métodos:
        __str__(): Retorna o nome do goleiro como uma string.
    """

    AVULSO = 1
    MENSALISTA = 2
    TIPOS_PESSOA_CHOICES = (
        (AVULSO, "Avulso"),
        (MENSALISTA, "Mensalista"),
    )

    tipo = models.IntegerField(
        default=1, choices=TIPOS_PESSOA_CHOICES, verbose_name="Tipo"
    )

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Jogador"
        verbose_name_plural = "Jogadores"


class Goleiro(Pessoa):
    """
    Representa um goleiro. Herda da classe Pessoa e adiciona um
    campo para o custo do goleiro. Possui os seguintes atributos:

    Atributos:
        nome (str): Nome completo do goleiro.
        telefone (str, opcional): Número de telefone do goleiro.
        pix (str, opcional): Chave Pix do goleiro.
        custo (Decimal): Custo do goleiro, em reais.

    Métodos:
        __str__(): Retorna o nome do goleiro como uma string.
    """

    custo = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.nome
