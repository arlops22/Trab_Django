from django.urls import path
from . import views

app_name = 'produto'

urlpatterns = [
    path('', views.index, name='index'),
    path('contato', views.contato, name='contato'),
    path('sobre', views.sobre, name='sobre'),
    path('cadastro', views.cadastro, name='cadastro'),

    path('show_produto/<int:id>/', views.show_produto, name='show_produto'),
    path('edit_produto/<int:id>/', views.edit_produto, name='edit_produto'),
    path('remove_produto/', views.remove_produto, name='remove_produto'),

    path('produto', views.lista_produto, name='produto'),
    path('produto/<slug:slug_da_categoria>/', views.lista_produto, name='lista_produtos_por_categoria'),
]