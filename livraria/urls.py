from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Usando view
    path('categorias/', views.CategoriaView.as_view()),
    path('categorias/<int:id>/', views.CategoriaView.as_view()),

    # Usando APIView ou ListAPIView
    path('categorias-api-view/', views.CategoriasList.as_view()),
    path('categorias-api-view/<int:id>/', views.CategoriaDetail.as_view()),
]
