from django.db import models

class Continente(models.Model):
    nome = models.CharField(max_length=50)

    def __str__ (self):
        return  self.nome
    

class Pais(models.Model):
    nome = models.CharField(max_length=50)
    nomeContinente = models.ForeignKey(Continente, on_delete=models.CASCADE)

    def __str__ (self):
        return  f'{self.nome}, {self.nomeContinente}'
    

class Temporada(models.Model):
    temp = models.CharField(max_length=20)

    def __str__ (self):
        return  self.temp
    

class AtorDiretor(models.Model):
    nome = models.CharField(max_length=100)
    site = models.CharField(max_length=100)
    insta = models.CharField(max_length=50)
    face = models.CharField(max_length=50)
    twitter = models.CharField(max_length=50)
    nacionalidade = models.ManyToManyField(Pais)

    def __str__ (self):
        return  f'{self.nome}, {self.site}, {self.insta}, {self.face}, {self.twitter}, {self.nacionalidade}'


class Genero(models.Model):
    nome = models.CharField(max_length=100)

    def __str__ (self):
        return  self.nome
    

class Filme(models.Model):
    nome = models.CharField(max_length=100)
    duracao = models.CharField(max_length=10)
    sinopse = models.CharField(max_length=300)
    siteOficial = models.CharField(max_length=50)
    dataLancamento = models.DateTimeField()
    notaAvaliacao = models.CharField(max_length=10)
    genero = models.ManyToManyField(Genero)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    diretor = models.ManyToManyField(AtorDiretor)

    def __str__ (self):
        return  f'{self.nome}, {self.duracao}, {self.sinopse}, {self.siteOficial}, {self.dataLancamento}, {self.notaAvaliacao}, {self.genero}, {self.pais}, {self.diretor}'

class Serie(models.Model):
    nome = models.CharField(max_length=100)
    duracao = models.CharField(max_length=30)
    sinopse = models.CharField(max_length=300)
    siteOficial = models.CharField(max_length=50)
    dataLancamento = models.DateTimeField()
    notaAvaliacao = models.CharField(max_length=10)
    genero = models.ManyToManyField(Genero)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    diretor = models.ManyToManyField(AtorDiretor)

    def __str__ (self):
        return  f'{self.nome}, {self.duracao}, {self.sinopse}, {self.siteOficial}, {self.dataLancamento}, {self.notaAvaliacao}, {self.genero}, {self.pais}, {self.diretor}'


class Episodio(models.Model):
    nome = models.CharField(max_length=100)
    duracao = models.CharField(max_length=30)

    def __str__ (self):
        return  f'{self.nome}, {self.duracao}'


class SerieEp(models.Model):
    serie = models.ForeignKey(Serie, on_delete=models.CASCADE)
    temp = models.ManyToManyField(Temporada)
    ep = models.ManyToManyField(Episodio)

    def __str__ (self):
        return  f'{self.serie}, {self.temp}, {self.ep}'
    

class FilmeAtor(models.Model):
    filme = models.ForeignKey(Filme, on_delete=models.CASCADE)
    ator = models.ManyToManyField(AtorDiretor)

    def __str__ (self):
        return  f'{self.filme}, {self.ator}'

