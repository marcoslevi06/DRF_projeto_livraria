from django.urls import path, include
from rest_framework import routers
from django.contrib import admin

from core.views.testes_iniciais import *
from core.views.categoriaGeneric import *
from core.views.categoriaAPIView import *
from core.views.categoriaClass import *
from core.views.viewSets import *

router = routers.DefaultRouter()
router.register(r'categorias-viewset', CategoriaViewSet)
router.register(r'editoras-viewset', EditoraViewSet)
router.register(r'autores-viewset', AutorViewSet)
router.register(r'livro-viewset', LivroViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    # Página 1 e 2
    path('pag1/', teste1, name='teste1'),
    path('pag2/', teste2, name='teste2'),

    # Usando view
    path('categorias/', CategoriaView.as_view()),
    path('categorias/<int:id>/', CategoriaView.as_view()),

    # Usando APIView ou ListAPIView
    path('categorias-api-view/', CategoriasList.as_view()),
    path('categorias-api-view/<int:id>/', CategoriaDetail.as_view()),

    # Usando Generics Views / ListCreateAPIView
    path('categorias-generic-view/', CategoriaListGeneric.as_view()),
    # Usando Gereric Views / RetrieveUpdateDestroyAPIView
    path('categorias-generic-view/<int:id>/',
         CategoriaDetailGeneric.as_view()),

    # Inclui as ViewSets que foram criadas
    path('', include(router.urls)),
]
