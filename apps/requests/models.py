from django.db import models
from clients.models import Client
from animals.models import Animal

class Request(models.Model):
# Create your models here.
    STATUS_CHOICES = (
        ('A', 'Aceito'),
        ('R', 'Recusado'),
        ('P', 'Pendente')
    )
    status = models.CharField('Status da solicitação', max_length=1, choices=STATUS_CHOICES, default='P')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Cliente')
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, verbose_name='Animal')
    created_at = models.DateTimeField('Data e Hora da Solicitação', auto_now_add=True)

    class Meta:
        verbose_name = 'Solicitacao'
        verbose_name_plural = 'Solicitacoes'

    def __str__(self):
        return f'{self.client} - {self.animal} - {self.get_status_display()}'