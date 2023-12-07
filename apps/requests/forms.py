from django import forms
from animals.models import Animal
from clients.models import Client
from .models import Request

class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        exclude = ()
           
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['animal'].queryset = Animal.objects.filter(is_adopted=False).order_by('name')
        self.fields['client'].queryset = Client.objects.order_by('first_name')