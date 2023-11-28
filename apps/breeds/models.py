from django.db import models
from species.models import Specie 

class Breed(models.Model):
    name = models.CharField('Nome', max_length=50, unique=True)
    description = models.TextField('Descricao', max_length=500)
    specie = models.ForeignKey(Specie, on_delete=models.CASCADE, verbose_name='Espécie')
    
    class Meta:
        verbose_name = 'Raca'
        verbose_name_plural = 'Racas'
        ordering =['id']

    def __str__(self):
        return f'{self.name} ({self.specie.name})'
