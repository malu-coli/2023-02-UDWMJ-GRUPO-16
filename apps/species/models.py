from django.db import models
from django.forms import ValidationError

class Specie(models.Model):
    name = models.CharField('Nome', max_length=50, unique=True)
    description = models.TextField('Descricao', max_length=100)

    class Meta:
        verbose_name = 'Especie'
        verbose_name_plural = 'Especies'
        ordering =['id']

    def __str__(self):
        return self.name
    
    def validate_unique(self, exclude=None):
        if Specie.objects.exclude(id=self.id).filter(name=self.name).exists():
            raise ValidationError({'name': 'Esta espécie já está cadastrada.'})
        super().validate_unique(exclude)