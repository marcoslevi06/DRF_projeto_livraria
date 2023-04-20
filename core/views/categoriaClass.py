from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
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
