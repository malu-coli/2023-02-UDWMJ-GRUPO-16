from django.db import models
from clients.models import Client
from animals.models import Animal

class Request(models.Model):
# Create your models here.
    STATUS_CHOICES = (
        ('A', 'Aceito'),
        ('R', 'Recusado')
    )
    status = models.CharField('Status da solicitacao', max_length=1, choices=STATUS_CHOICES)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Cliente')
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, verbose_name='Animal')

    class Meta:
        verbose_name = 'Solicitacao'
        verbose_name_plural = 'Solicitacoes'

    def str(self):
        return self.status