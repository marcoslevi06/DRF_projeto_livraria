from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from core.serializer import *
from core.models import *


class CategoriasList(APIView):
    '''
    Listando todas as categorias com rest_framework.
    Class based views com APIView;

    1 definir o método
    2 criar uma variável de instância que recebe todos os objetos do model
    3 criar variável de instância que recebe os dados serializados
    4 retornar uma resposta Http com os dados serializados
    '''

    def get(self, request):
        categorias = Categoria.objects.all()
        serializer = CategoriaSerializer(categorias, many=True)

        print('\ncategorias = ', categorias)
        print('\nserializer = ', serializer)
        print('\nResponse = ', Response(serializer.data))
        return Response(serializer.data)

    def post(self, request):
        '''
        Enviando os dados via método/verbo POST.

        1 Ler o que está no corpo da requisição
        2 Saber se ele é válido ou não para salvá-lo
            3 Salvar e retornar uma resposta Http
        4 Se não for válido, retornar uma resposta Http de erro.
        '''

        serializer = CategoriaSerializer(data=request.data)
        print('serializer =', serializer)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoriaDetail(APIView):
    '''
    Pegando os detalhes de um objeto

    1 criar variavel de instancia que rebece o objeto identificado pelo ID OU (PK)
    2 criar variavel de instancia para receber o objeto serializado
    3 retornar uma resposta Http com o que foi serializado
    '''

    def get(self, request, id):
        categoria = get_object_or_404(Categoria.objects.all(), id=id)
        serializer = CategoriaSerializer(categoria)
        return Response(serializer.data)

    def put(self, request, id):
        '''
        1 criar var de inst. que recebe o objeto identificado pelo id ou (pk)
        2 criar var de inst. que recebe o objeto serializado
        3 validar esse objeto e salvá-lo
            4 retornar uma resposta Http com o objeto
        4 se não for válido, retornar uma resposta Http com mensagem de erro
        '''
        categoria = get_object_or_404(Categoria.objects.all(), id=id)
        serializer = CategoriaSerializer(categoria, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        '''
        1 criar var. de inst. que recebe o objeto
        2 deletar o objeto criar var. de inst. que recebe o objetoe retornar uma resposta Http
        '''
        categoria = get_object_or_404(Categoria.objects.all(), id=id)
        categoria.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
