from django.shortcuts import render
from .models import Breed
from rest_framework import viewsets
from .serializer import BreedSerializer
from .forms import BreedForm
from .models import Breed
from django.shortcuts import render, get_object_or_404, redirect

class BreedViewSet(viewsets.ModelViewSet):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer


def add_breed(request):
    template_name = 'breeds/add_breed.html'
    context = {}
    if request.method == 'POST':
        form = BreedForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('breeds:list_breeds')
    form = BreedForm()
    context['form'] = form
    return render(request, template_name, context)

def list_breeds(request):
    template_name = 'breeds/list_breeds.html'
    breeds = Breed.objects.filter()
    context = {
        'breeds': breeds
    }
    return render(request, template_name, context)

def edit_breed(request, id_breed):
    template_name = 'breeds/add_breed.html'
    context ={}
    breed = get_object_or_404(Breed, id=id_breed)
    if request.method == 'POST':
        form = BreedForm(request.POST, instance=breed)
        if form.is_valid():
            form.save()
            return redirect('breeds:list_breeds')
    form = BreedForm(instance=breed)
    context['form'] = form
    return render(request, template_name, context)

def delete_breed(request, id_breed):
    breed = Breed.objects.get(id=id_breed)
    breed.delete()
    return redirect('breeds:list_breeds')