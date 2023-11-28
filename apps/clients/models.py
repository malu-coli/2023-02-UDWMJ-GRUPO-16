from django.core.exceptions import ValidationError
from django.db import models
from localflavor.br.models import BRCPFField

class Client(models.Model):
    first_name = models.CharField('Primeiro Nome', max_length=50)
    last_name = models.CharField('Sobrenome', max_length=50)
    address = models.TextField('Endereço', max_length=255)
    cell_phone = models.CharField('Número de Celular', max_length=15, unique=True)
    email = models.EmailField('Endereço de Email', unique=True)
    suid = BRCPFField('CPF', unique=True)
    GENDER_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro')
    )
    gender = models.CharField('Gênero', max_length=1, choices=GENDER_CHOICES)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['id']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def validate_unique(self, exclude=None):
        if Client.objects.exclude(id=self.id).filter(cell_phone=self.cell_phone).exists():
            raise ValidationError({'cell_phone': 'Este número de celular já está em uso.'})
        if Client.objects.exclude(id=self.id).filter(email=self.email).exists():
            raise ValidationError({'email': 'Este endereço de e-mail já está em uso.'})
        if Client.objects.exclude(id=self.id).filter(suid=self.suid).exists():
            raise ValidationError({'CPF': 'Este CPF já está cadastrado.'})
        super().validate_unique(exclude)