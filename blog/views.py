from django.shortcuts import render
from .models import Eu, Filmes, Series
# Create your views here.
def index(request):
    filme = Filmes.objects.all()
    serie = Series.objects.all()
    contexto = {
        'filmes' : filme,
        'series' : serie
    }
    
    return render(request, 'blog/index.html', contexto)

def SobreFilme(request, filmes_id):
    detalhe = Filmes.objects.get(id=filmes_id)
    contexto = {
        'detalhe' : detalhe
    }
    
    return render(request, 'blog/sobrefilme.html', contexto)

def SobreSerie(request, serie_id):
    detalhe2 = Series.objects.get(id=serie_id)
    contexto = {
        'detalhe2' : detalhe2,
    }
    
    return render(request, 'blog/sobreserie.html', contexto)