from django.db import models
from django.contrib.auth.models import User


class Categoria(models.Model):
    descricao = models.CharField(max_length=255)

    def __str__(self):
        return self.descricao


class Montadora(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome


class Motorista(models.Model):
    nome = models.CharField(max_length=255)
    cnh = models.IntegerField()

    def __str__(self):
        return self.nome


class Veiculo(models.Model):
    modelo = models.CharField(max_length=255)
    chassi = models.CharField(max_length=17)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    ano = models.IntegerField()
    categoria = models.ForeignKey(
        Categoria, on_delete=models.PROTECT, related_name="veiculos")
    montadora = models.ForeignKey(
        Montadora, on_delete=models.PROTECT, related_name="veiculos")
    motorista = models.ManyToManyField(Motorista, related_name="veiculos")

    def __str__(self):
        return "%s chassi(%s)" % (self.modelo, self.chassi)


class Acompanhamento(models.Model):
    class StatusFrota(models.IntegerChoices):
        SAIDA = 1, "Saída da Portaria"
        ONROAD = 2, "A caminho"
        ENTREGUE = 3, "Entregue na portaria"
        RETORNO = 4, "Viagem de retorno Iniciada"
        CEDE = 5, "Se encontra na cede"

    veiculo = models.ForeignKey(
        Veiculo, on_delete=models.PROTECT, related_name="acompanhamento")
    status = models.IntegerField(
        choices=StatusFrota.choices, default=StatusFrota.CEDE)


class ItensEntrega(models.Model):
    acompanhamento = models.ForeignKey(
        Acompanhamento, on_delete=models.CASCADE, related_name="itens")
    veiculo = models.ForeignKey(
        Veiculo, on_delete=models.PROTECT, related_name="+")
    quantidade = models.IntegerField()
