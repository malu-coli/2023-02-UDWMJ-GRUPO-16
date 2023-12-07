from django import forms
from .models import Animal
from breeds.models import Breed
from species.models import Specie

class AnimalForm(forms.ModelForm):

    class Meta:
        model = Animal
        fields = ['name', 'age', 'description', 'specie', 'breed', 'color', 'gender', 'is_adopted', 'image']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }
        exclude: ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['specie'].queryset = Specie.objects.order_by('name')
        self.fields['breed'].queryset = Breed.objects.order_by('name')