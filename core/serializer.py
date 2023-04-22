from rest_framework import serializers
from core.models import *


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        exclude = []


class EditoraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editora
        exclude = []


class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        exclude = []


class LivroSerializer (serializers.ModelSerializer):
    class Meta:
        model = Autor
        exlcude = []