from django.http import HttpResponse
from core.serializer import *
from core.models import *


def teste1(request):
    return HttpResponse('Olá, essa é a página 1')


def teste2(request):
    return HttpResponse('Olá, essa é a página número 2')
