from django.http import HttpResponse, JsonResponse


from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.views import View
from core.serializer import *
from core.models import *
import json


@method_decorator(csrf_exempt, name='dispatch')
class CategoriaView(View):

    def get(self, request, id=None):
        if id:
            queryset = Categoria.objects.get(id=id)
            data = {}
            data['id'] = queryset.id
            data['descricao'] = queryset.descricao
            print(data)
            return JsonResponse(data)
        else:
            data = list(Categoria.objects.values())
            formatted_data = json.dumps(data, ensure_ascii=False)

            # Verificando as variáveis
            print('\nDados = ', data)
            print('\nDados formatados = ', formatted_data)
            return HttpResponse(formatted_data, content_type='application/json')

    def post(self, request):
        ''' 
        Ler objeto, criar objeto em formato Json e depois retornar objeto. 
        '''
        json_data = json.loads(request.body)
        nova_categoria = Categoria.objects.create(**json_data)
        return JsonResponse(nova_categoria)

    def patch(self, request, id):
        '''
        Ler o objeto Json. Atribuir o objeto especificado ao queryset.
        queryset.decricao recebe a nova descricao alterada no corpo da requisicao
        '''
        json_data = json.loads(request.body)
        queryset = Categoria.objects.get(id=id)
        # if 'descricao' in json_data else queryset.descricao
        queryset.descricao = json_data['descricao']
        queryset.save()
        data = {}
        data['id'] = queryset.id
        data['descricao'] = queryset.descricao
        return JsonResponse(data)

    def delete(self, request, id):
        objeto = Categoria.objects.get(id=id)
        objeto.delete()
        data = {'mensagem': 'item excluído com sucesso'}
        return JsonResponse(data)


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


class CategoriaListGeneric(ListCreateAPIView):
    '''Lista todas as categorias criadas'''
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class CategoriaDetailGeneric(RetrieveUpdateDestroyAPIView):
    # Campo de busca será o Id. Com o lookup_field é possível forçar a busca pela str especificada
    lookup_field = 'id'
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
