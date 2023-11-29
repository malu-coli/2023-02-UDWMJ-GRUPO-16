from django.shortcuts import render
from .models import Request
from rest_framework import viewsets
from .serializer import RequestSerializer

class RequestViewSet(viewsets.ModelViewSet):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer