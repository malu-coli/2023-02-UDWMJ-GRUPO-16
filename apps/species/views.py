from django.shortcuts import render
from .models import Specie
from rest_framework import viewsets
from .serializer import SpecieSerializer
from django.shortcuts import render, get_object_or_404, redirect
from .forms import SpecieForm
from .models import Specie

class SpecieViewSet(viewsets.ModelViewSet):
    queryset = Specie.objects.all()
    serializer_class = SpecieSerializer

def add_specie(request):
    template_name = 'species/add_specie.html'
    context = {}
    if request.method == 'POST':
        form = SpecieForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('species:list_species')
    form = SpecieForm()
    context['form'] = form
    return render(request, template_name, context)

def list_species(request):
    template_name = 'species/list_species.html'
    species = Specie.objects.filter()
    context = {
        'species': species
    }
    return render(request, template_name, context)

def edit_specie(request, id_specie):
    template_name = 'species/add_specie.html'
    context ={}
    specie = get_object_or_404(Specie, id=id_specie)
    if request.method == 'POST':
        form = SpecieForm(request.POST, instance=specie)
        if form.is_valid():
            form.save()
            return redirect('species:list_species')
    form = SpecieForm(instance=specie)
    context['form'] = form
    return render(request, template_name, context)

def delete_specie(request, id_specie):
    specie = Specie.objects.get(id=id_specie)
    specie.delete()
    return redirect('species:list_species')