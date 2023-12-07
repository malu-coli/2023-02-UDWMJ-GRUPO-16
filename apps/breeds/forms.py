from django import forms
from .models import Breed
from species.models import Specie

class BreedForm(forms.ModelForm):

    class Meta:
        model = Breed
        exclude = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['specie'].queryset = Specie.objects.order_by('name')