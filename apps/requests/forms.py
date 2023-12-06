from django import forms
from animals.models import Animal
from .models import Request

class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        exclude = ()
           
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['animal'].queryset = Animal.objects.filter(is_adopted=False)