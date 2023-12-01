from django import forms
from .models import Animal

class AnimalForm(forms.ModelForm):

    class Meta:
        model = Animal
        fields = ['name', 'age', 'description', 'specie', 'breed', 'color', 'gender', 'is_adopted', 'image']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }
        exclude: ()