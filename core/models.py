from django.db import models

# Create your models here.


class Categoria(models.Model):
    descricao = models.CharField(max_length=255, verbose_name='Descrição')

    def __str__(self) -> str:
        return f'{self.descricao}'


class Editora(models.Model):
    nome = models.CharField(max_length=255, verbose_name='Nome')
    site = models.URLField(max_length=255, verbose_name='Site')

    def __str__(self) -> str:
        return f'{self.nome}'


class Autor(models.Model):
    class Meta:
        verbose_name_plural = 'Autores'

    nome = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f'{self.nome}'


class Livro(models.Model):
    class Meta:
        verbose_name_plural = 'Livros'

    titulo = models.CharField(max_length=255)
    ISBN = models.CharField(max_length=255)
    quantidade = models.IntegerField()
    preco = models.FloatField()
    categoria = models.ForeignKey(
        Categoria, on_delete=models.PROTECT, related_name='livros')
    editora = models.ForeignKey(
        Editora, on_delete=models.PROTECT, related_name='livros')
    autores = models.ManyToManyField(Autor, related_name='livros')

    def __str__(self) -> str:
        return f'{self.titulo}/{self.editora}'