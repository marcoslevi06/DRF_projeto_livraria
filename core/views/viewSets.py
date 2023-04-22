from rest_framework import viewsets
from core.serializer import *
from core.models import *


class CategoriaViewSet(viewsets.ModelViewSet):
    '''
    Criando um CRUD completo e genérico com ViewSet
    '''
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class EditoraViewSet(viewsets.ModelViewSet):
    '''
    CRUD de Editora
    '''
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer


class AutorViewSet(viewsets.ModelViewSet):
    '''
    CRUD Autor
    '''
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer


class LivroViewSet(viewsets.ModelViewSet):
    '''
    CRUD Livro
    '''
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
