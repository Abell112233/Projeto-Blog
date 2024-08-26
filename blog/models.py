from django.db import models

# Create your models here.
class Filmes(models.Model):
    nome = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='filmes', null=True, blank=True)
    descricao = models.TextField()
    
    def __str__(self):
        return self.nome

class Series(models.Model):
    nome = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='series', null=True, blank=True)
    descricao = models.TextField()
    
    def __str__(self):
        return self.nome
    
