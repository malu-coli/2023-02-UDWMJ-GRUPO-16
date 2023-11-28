from django.shortcuts import render
from .models import Breed
from rest_framework import viewsets
from .serializer import BreedSerializer

class BreedViewSet(viewsets.ModelViewSet):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer