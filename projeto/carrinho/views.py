from django.shortcuts import render, get_object_or_404
from carrinho.carrinho import Carrinho
from carrinho.forms import QuartosForm, RemoveProdutoDoCarrinhoForm
from produto.models import Produto

# Create your views here.


def exibe_compra(request, id):
    produto = get_object_or_404(Produto, id=id)
    return render(request, 'carrinho/compra.html', {'produto': produto,})


def exibe_carrinho(request):
    return render(request, 'carrinho/carrinho_compras.html' )
    

def produto_carrinho(request, id):
    produto = get_object_or_404(Produto, id=id)

    return render(request, 'carrinho/objeto.html', {'produto': produto
})


def carrinho(request):
    carrinho = Carrinho(request)

    lista_de_produtos_no_carrinho = carrinho.get_produtos()

    produtos_no_carrinho = []
    lista_de_forms = []
    for item in lista_de_produtos_no_carrinho:
        produtos_no_carrinho.append(item['produto'])
    
    return render(request, 'carrinho/carrinho.html',  {
       'listas': zip(produtos_no_carrinho, lista_de_forms),
    })

def adicionar_ao_carrinho(request):
    form = QuartosForm(request.POST)
    if form.is_valid():
        quartos = 1
        produto_id = form.cleaned_data['produto_id']

        carrinho = Carrinho(request)
        carrinho.adicionar(produto_id, quartos)

        return carrinho(request)
    else:
        print(form.errors)
        raise ValueError('Ocorreu um erro inesperado ao adicionar um produto ao carrinho.')


def remove_produto_carrinho(request):
    form = RemoveProdutoDoCarrinhoForm(request.POST)
    if form.is_valid():
        carrinho = Carrinho(request)
        carrinho.remover(form.cleaned_data['produto_id'])

        return carrinho(request)
    else:
        print(form.errors)
        raise ValueError('Ocorreu um erro inesperado ao adicionar um produto ao carrinho.')


def atualiza_qtd_carrinho(request):
    form = QuartosForm(request.POST)
    if form.is_valid():
        produto_id = form.cleaned_data['produto_id']
        quartos =  form.cleaned_data['quartos']

        carrinho = Carrinho(request)
        carrinho.alterar(produto_id, quartos)

        return carrinho(request)
    else:
        print(form.errors)
        raise ValueError('Ocorreu um erro inesperado ao adicionar um produto ao carrinho.')
