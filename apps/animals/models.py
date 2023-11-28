from django.db import models
from django.forms import ValidationError
from breeds.models import Breed
from species.models import Specie

class Animal(models.Model):
    name = models.CharField('Nome', max_length=50)
    description = models.TextField('Descricao', max_length=100)
    age = models.IntegerField('Idade')
    specie = models.ForeignKey(Specie, on_delete=models.CASCADE,verbose_name='Espécie')
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE, verbose_name='Raça')
    color = models.TextField('Cor', max_length=100)
    GENDER_CHOICES = (
        ('M', 'Macho'),
        ('F', 'Fêmea')
    )
    gender = models.CharField('Genero', max_length=1, choices=GENDER_CHOICES)
    is_adopted = models.BooleanField('Adotado', default=False)
    image = models.ImageField('Fotinho', upload_to='animal_images/', null=True, blank=True)
    
    class Meta:
        verbose_name = 'Animal'
        verbose_name_plural = 'Animais'
        ordering =['id']

    def __str__(self):
        return self.name
    
    def clean(self):
        if self.breed.specie != self.specie:
            raise ValidationError('A raça não pertence à esta espécie.')

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
