from django.db import models

class Specie(models.Model):
    name = models.CharField('Nome', max_length=50, unique=True)
    description = models.TextField('Descricao', max_length=100)

    class Meta:
        verbose_name = 'Especie'
        verbose_name_plural = 'Especies'
        ordering =['id']

    def __str__(self):
        return self.name