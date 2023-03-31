from django.urls import path
from . import views

urlpatterns = [
    path('produtos', view=views.ProdutoList.as_view()),
    path('categorias', view=views.Categoria.as_view())
]