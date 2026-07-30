from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    ativo = models.BooleanField(default=True)


class Servico(models.Model):
    nome = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    duracao = models.IntegerField()
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        null=True
    )
    ativo = models.BooleanField(default=True)