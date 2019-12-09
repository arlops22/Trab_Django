from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Categoria, Produto, Informacoes
from produto.forms import ProdutoForm, RemoveProdutoForm, PesquisaProdutoForm
from django.contrib.auth.models import User
from carrinho.carrinho import Carrinho
from carrinho.forms import QuartosForm

# Create your views here.

def index(request):
    categoria = Categoria.objects.all().order_by("id")
    produtos = Produto.objects.filter(categoria=1).order_by("nome")
    return render(request, 'produto/home.html', {'categoria': categoria, 'produtos': produtos})

def contato(request):
    titulo = 'Fale Conosco'
    return render(request, 'produto/contato.html', {'titulo': titulo})


def sobre(request):
    informacoes = Informacoes.objects.all().order_by('id')
    titulo = "Sobre nós"
    return render(request, 'produto/sobre.html', {'informacoes': informacoes, 'titulo': titulo})


def lista_produto(request, slug_da_categoria=None):
   form = PesquisaProdutoForm(request.GET)
   categoria = None
   titulo = "Produtos"
   categorias = Categoria.objects.all().order_by("id")
   produtos = Produto.objects.filter(disponivel=True).order_by("nome")
   if slug_da_categoria:
      categoria = get_object_or_404(Categoria, slug=slug_da_categoria)
      produtos = produtos.filter(categoria=categoria).order_by("nome")
   
   elif (form.is_valid()):
      categoria = None
      busca_por = form.cleaned_data['busca_por']
      produtos = Produto.objects.filter(nome__icontains=busca_por).order_by('nome')

   return render(request, 'produto/produto.html', {'categorias': categorias,
                                                'produtos': produtos,
                                                'categoria': categoria,
                                                'form': form, 
                                                'titulo': titulo})

def cadastro(request):
    produto_id = request.POST.get("produto_id", None)
    if request.POST:
      if produto_id:
         produto = get_object_or_404(Produto, id=produto_id)
         form = ProdutoForm(request.POST, instance=produto)
      else:   
         form = ProdutoForm(request.POST)

      if form.is_valid():
         produto = form.save()
         if produto_id:
            messages.add_message(request, messages.INFO, 'Produto alterado com sucesso.')            
         else:
            messages.add_message(request, messages.INFO, 'Produto cadastrado com sucesso.')               

         return redirect('produto:show_produto', id=produto.id)
      else:
         messages.add_message(request, messages.ERROR, 'Corrija o(s) erro(s) abaixo:')               
    else:
      form = ProdutoForm()
   
    return render(request, 'produto/cadastro.html', {'form': form})


def show_produto(request, id):   
   produto = get_object_or_404(Produto, id=id)
   form_remove_produto = RemoveProdutoForm(initial={'produto_id': id})
   return render(request, 'produto/show_produto.html', {
      'produto': produto,
      'form_remove_produto': form_remove_produto,
   })

def edit_produto(request, id):
   produto = get_object_or_404(Produto, pk=id)
   form = ProdutoForm(instance=produto)
   form.fields['produto_id'].initial=id
   return render(request, 'produto/cadastro.html', {'form': form})

def remove_produto(request):
#   form_remove_produto = RemoveProdutoForm(request.POST)
#   if form_remove_produto.is_valid:
      # produto_id = form_remove_produto.cleaned_data['produto_id']
      produto_id = request.POST.get('produto_id')
      produto = get_object_or_404(Produto, id=produto_id)
      produto.delete()
      messages.add_message(request, messages.INFO, 'Produto removido com sucesso.')
      return render(request, 'produto/show_produto.html', {'produto': produto})
#   else:
#      raise ValueError('Ocorreu um erro inesperado ao tentar remover um produto.')

