from django.shortcuts import render
from .models import Specie
from rest_framework import viewsets
from .serializer import SpecieSerializer

class SpecieViewSet(viewsets.ModelViewSet):
    queryset = Specie.objects.all()
    serializer_class = SpecieSerializer