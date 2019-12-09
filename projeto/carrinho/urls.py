from django.urls import path
from . import views

app_name = 'carrinho'

urlpatterns = [
    path('exibe_compra/<int:id>/', views.exibe_compra, name='exibe_compra'),
    path('carrinho/', views.carrinho, name='carrinho'),
    path('exibe_carrinho/', views.exibe_carrinho, name='exibe_carrinho'),
    path('adicionar_ao_carrinho/', views.adicionar_ao_carrinho, name='adicionar_ao_carrinho'),
    path('remove_produto_carrinho/', views.remove_produto_carrinho, name='remove_produto_carrinho'),
    path('produto_carrinho/<int:id>/', views.produto_carrinho, name='produto_carrinho'),
    path('atualiza_qtd_carrinho/', views.atualiza_qtd_carrinho, name='atualiza_qtd_carrinho'),
]
