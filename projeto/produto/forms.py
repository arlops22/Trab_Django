from decimal import Decimal
from django import forms
from django.core.validators import RegexValidator
from produto.models import Produto, Categoria

class ProdutoForm(forms.ModelForm):

    class Meta:
        model = Produto
        fields = ('produto_id', 'categoria', 'nome', 'imagem', 'quartos', 'preco','descricao')

    produto_id = forms.CharField(widget=forms.HiddenInput(), required=False)

    categoria = forms.ModelChoiceField(
        error_messages={'required': 'Campo obrigatório.', },
        queryset=Categoria.objects.all().order_by('id'),
        empty_label='--- Selecione um(a) categoria ---',
        widget=forms.Select(attrs={'class': 'form-control form-control-sm'}),
        required=True) 

    nome = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'maxlength': '60'}),
        required=True)  

    imagem = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'maxlength': '60'}),
        required=False)     

    preco = forms.CharField(
        localize=True,
        error_messages={'required': 'Campo obrigatório.', },
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm',
            'maxlength': '10',
            'onkeypress': 'return (event.charCode >= 48 && event.charCode <= 57) || event.charCode == 44'}),
        required=True)

    quartos = forms.CharField(
        validators=[RegexValidator(regex='^[0-9]{1,5}$', message="Informe o valor no formato 99999.")],
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm',
                                      'maxlength': '5',
                                      'onkeypress': 'return event.charCode >= 48 && event.charCode <= 57'}),
        required=False)
      

    descricao = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control form-control-sm', 'cols': '40', 'rows': '5'}),
        required=False)

class RemoveProdutoForm(forms.Form):
    class Meta:
        fields = ('produto_id')

    produto_id = forms.CharField(widget=forms.HiddenInput(), required=True)

    # <input type="hidden" name="produto_id" id="id_produto_id" value="xxx">

class PesquisaProdutoForm(forms.Form):
   class Meta:
      fields = ('busca_por')

   busca_por = forms.CharField(
      widget=forms.TextInput(attrs={'placeholder': 'Nome da Moradia', 'class': 'form-control form-control-sm', 'maxlength': '120'}),
      required=False)
   
   # <input type='text'
   #        name='busca_por'
   #        id='id_busca_por'
   #        class='form-control form-control-sm'
   #        maxlength='120'>   
