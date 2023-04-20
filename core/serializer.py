from rest_framework import serializers
from core.models import *


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        exclude = []
