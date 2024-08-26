from django.shortcuts import render
from .models import Eu, Filmes, Series
# Create your views here.
def index(request):
    filmes = Filmes.objects.all()
    series = Series.objects.all()
    contexto = {
        "filmes" : filmes,
        "series" : series
    }
    
    return render(request, 'blog/index.html', contexto)
