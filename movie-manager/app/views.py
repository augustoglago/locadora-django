from django.shortcuts import render
from . models import *

def consultaFilme(request):
    consultaFilmes = {
        'filmes': Filme.objects.all(),
    }

    return render(request, 'consulta/consultaFilme.html', consultaFilmes)
