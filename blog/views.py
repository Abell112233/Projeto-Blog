from django.shortcuts import render
from .models import Eu, Filmes, Series
# Create your views here.
def index(request):
    eu = Eu.objects.all()
    contexto = {
        "eu" : eu
    }
    
    return render(request, 'blog/index.html', contexto)