from django.urls import path, include
from rest_framework import routers
from django.contrib import admin

from core.views.categoriaGeneric import *
from core.views.categoriaViewSet import *
from core.views.categoriaAPIView import *
from core.views.categoriaClass import *

router = routers.DefaultRouter()
router.register(r'categorias-viewset', CategoriaViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),

    # Usando view
    path('categorias/', CategoriaView.as_view()),
    path('categorias/<int:id>/', CategoriaView.as_view()),

    # Usando APIView ou ListAPIView
    path('categorias-api-view/', CategoriasList.as_view()),
    path('categorias-api-view/<int:id>/', CategoriaDetail.as_view()),

    # Usando Generics Views / ListCreateAPIView
    path('categorias-generic-view/', CategoriaListGeneric.as_view()),
    # Usando Gereric Views / RetrieveUpdateDestroyAPIView
    path('categorias-generic-view/<int:id>/', CategoriaDetailGeneric.as_view()),

    path('', include(router.urls)),
]
