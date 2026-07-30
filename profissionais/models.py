from django.db import models
from servicos.models import Servico

class Profissional(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    ativo = models.BooleanField(default=True)
    servicos = models.ManyToManyField(Servico)