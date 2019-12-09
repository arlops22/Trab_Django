from django.db import models
from django.urls import reverse
from django.conf import settings

class Categoria(models.Model):
    nome = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    imagem = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)

    class Meta:
        db_table='categoria'

    def get_absolute_path(self):
        return reverse('produto:lista_produtos_por_categoria', args=[self.slug])

    def __str__(self):
        return self.nome


class Produto(models.Model):
    categoria = models.ForeignKey(Categoria, related_name='produtos', on_delete=models.DO_NOTHING)
    nome = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    imagem = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=20, decimal_places=2)
    disponivel = models.BooleanField(default=True)
    quartos = models.IntegerField(default=0)

    class Meta:
        db_table = 'produto'

    def get_absolute_path(self):
        return reverse('produto:show_produto', args=[self.slug, self.id])

    def __str__(self):
        return self.nome

class Informacoes(models.Model):
    nome = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    descricao = models.TextField(blank=True)

    class Meta:
        db_table = 'informacoes'

    def get_absolute_path(self):
        return reverse('informacoes:exibe_informacoes', args=[self.slug])

    def __str__(self):
        return self.nome