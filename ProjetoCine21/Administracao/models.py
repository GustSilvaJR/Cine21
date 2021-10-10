from django.db import models

from Cadastro.models import Usuario

# Create your models here.

AVALIACAO = [
    ("1","1 Estrela"),
    ("2","2 Estrelas"),
    ("3","3 Estrelas"),
    ("4","4 Estrelas"),
    ("5","5 Estrelas"),
]

CLASSIFICACAO = [
    ("L","Livre"),
    ("I","Infantil"),
    ("12","Maiores de 12 Anos"),
    ("16","Maiores de 16 Anos"),
    ("18","Maiores de 18 Anos"),
]

class Genero(models.Model):
    nome = models.CharField('Nome do Gênero', max_length=20, null=False, blank=False) #Max length é obrigatório de colocar para evitar que de pala no codigo
    dataCadastro = models.DateTimeField('Hora do cadastro', auto_now_add=True)

    #null = False -> Eu não permito que seja salvo algum dado null; 

    #blank = False -> Faço com que o campo seja obrigatório;

    class Meta:
        verbose_name = "Gênero"
        verbose_name_plural = "Gêneros"
        ordering = ['nome']

    def __str__(self):
        return self.nome

class Filme(models.Model):
    nome = models.CharField('Nome do Filme', max_length=100, null=False, blank=False)

    dataLanca = models.DateTimeField('Data de Lançamento') #Só isso de info ?

    descricao = models.CharField('Sinopse', max_length=500, null=False, blank=False)

    image = models.ImageField("Imagem", upload_to = None , height_field = None , width_field = None , max_length = 100)

    autor = models.CharField('Autor', max_length=100, null=False, blank=False)

    roteirista = models.CharField('Roteirista', max_length=100, null=False, blank=False)

    direcao = models.CharField('Direção', max_length=100, null=False, blank=False)

    pais = models.CharField('País', max_length=50, null=False, blank=False)

    classificacao = models.CharField('Gênero', choices=CLASSIFICACAO, max_length=100)

    duracao = models.IntegerField('Duração') #Só isso de info ?

    avaliacao = models.CharField('Avaliação', choices=AVALIACAO, max_length=100)

    produtora = models.CharField('Produtora', max_length=80)

    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)

    autorPublish = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    createAt = models.DateTimeField('Criado em', auto_now_add=True)

    updateAt = models.DateTimeField('Atualizado em', auto_now_add=True)


    class Meta:
        verbose_name = "Filme"
        verbose_name_plural = "Filmes"
        ordering = ['nome']

    def __str__(self):
        return self.nome

class Serie(models.Model):
    nome = models.CharField('Nome da Serie', max_length=100, null=False, blank=False)

    dataLanca = models.DateTimeField('Data de Lançamento') #Só isso de info ?

    descricao = models.CharField('Sinopse', max_length=500, null=False, blank=False)

    image = models.ImageField("Imagem", upload_to = None , height_field = None , width_field = None , max_length = 100)#???? isso ai  ?

    temporadas = models.IntegerField("Temporadas")

    autor = models.CharField('Autor', max_length=100, null=False, blank=False)

    roteirista = models.CharField('Roteirista', max_length=100, null=False, blank=False)

    direcao = models.CharField('Direção', max_length=100, null=False, blank=False)

    pais = models.CharField('País', max_length=50, null=False, blank=False)

    classificacao = models.CharField('Gênero', choices=CLASSIFICACAO, max_length=100)

    duracao = models.IntegerField('Duração') #Só isso de info ?

    avaliacao = models.CharField('Avaliação', choices=AVALIACAO, max_length=100)

    produtora = models.CharField('Produtora', max_length=80)

    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)

    autorPublish = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    createAt = models.DateTimeField('Criado em', auto_now_add=True)

    updateAt = models.DateTimeField('Atualizado em', auto_now_add=True)


    class Meta:
        verbose_name = "Serie"
        verbose_name_plural = "Series"
        ordering = ['nome']

    def __str__(self):
        return self.nome 

class Anime (models.Model):
    nome = models.CharField('Nome do Anime', max_length=100, null=False, blank=False)

    dataLanca = models.DateTimeField('Data de Lançamento') #Só isso de info ?

    descricao = models.CharField('Sinopse', max_length=500, null=False, blank=False)

    image = models.ImageField("Imagem", upload_to = None , height_field = None , width_field = None , max_length = 100)#???? isso ai  ?

    temporadas = models.IntegerField("Temporadas")

    autor = models.CharField('Autor', max_length=100, null=False, blank=False)

    classificacao = models.CharField('Gênero', choices=CLASSIFICACAO, max_length=100)

    avaliacao = models.CharField('Avaliação', choices=AVALIACAO, max_length=100)

    produtora = models.CharField('Produtora', max_length=80)

    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)

    autorPublish = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    createAt = models.DateTimeField('Criado em', auto_now_add=True)

    updateAt = models.DateTimeField('Atualizado em', auto_now_add=True)


    class Meta:
        verbose_name = "Anime"
        verbose_name_plural = "Animes"
        ordering = ['nome']

    def __str__(self):
        return self.nome 

class Game(models.Model):
    nome = models.CharField('Nome do Jogo', max_length=100, null=False, blank=False)

    dataLanca = models.DateTimeField('Data de Lançamento') #Só isso de info ?

    descricao = models.CharField('Sinopse', max_length=500, null=False, blank=False)

    image = models.ImageField("Imagem", upload_to = None , height_field = None , width_field = None , max_length = 100)#???? isso ai  ?

    autor = models.CharField('Autor', max_length=100, null=False, blank=False)

    classificacao = models.CharField('Gênero', choices=CLASSIFICACAO, max_length=100)

    avaliacao = models.CharField('Avaliação', choices=AVALIACAO, max_length=100)

    produtora = models.CharField('Produtora', max_length=80)

    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)

    autorPublish = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    createAt = models.DateTimeField('Criado em', auto_now_add=True)

    updateAt = models.DateTimeField('Atualizado em', auto_now_add=True)


    class Meta:
        verbose_name = "Game"
        verbose_name_plural = "Games"
        ordering = ['nome']

    def __str__(self):
        return self.nome 