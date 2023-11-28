from .models import Breed
from rest_framework import serializers

class BreedSerializer(serializers.ModelSerializer):
    specie_name = serializers.CharField(source='specie.name', read_only=True)

    class Meta:
        model = Breed
        fields = ['id', 'name', 'description', 'specie', 'specie_name']