from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from core.serializer import *
from core.models import *


class CategoriaListGeneric(ListCreateAPIView):
    '''Lista todas as categorias criadas'''
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class CategoriaDetailGeneric(RetrieveUpdateDestroyAPIView):
    # Campo de busca será o Id. Com o lookup_field é possível forçar a busca pela str especificada
    lookup_field = 'id'
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
