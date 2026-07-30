from django.db import models
from clientes.models import Cliente
from servicos.models import Servico
from profissionais.models import Profissional


class Agendamento(models.Model):
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE
    )

    profissional = models.ForeignKey(
        Profissional,
        on_delete=models.CASCADE
    )

    servico = models.ForeignKey(
        Servico,
        on_delete=models.CASCADE
    )

    data = models.DateField()
    horario = models.TimeField()

    STATUS_CHOICES = [
        ('agendado', 'Agendado'),
        ('confirmado', 'Confirmado'),
        ('concluido', 'Concluído'),
        ('cancelado', 'Cancelado'),
    ]

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='agendado'
    )