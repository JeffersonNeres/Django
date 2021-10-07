from django.db import models
from datetime import datetime as dt

# Create your models here.

class FilmesFavorito(models.Model):
    #colunas do banco de dados
    classificação_CHOICES = (
    ('18', 'Apenas maiores de 18 anos'),
    ('16', 'Apenas maiores de 16 anos'),
    ('Livre', 'Livre para todas idades')
    )
    nome_do_filme = models.CharField(max_length=50)
    ator_principal = models.CharField(max_length=50)
    sinopse_do_filme = models.TextField()
    classificação = models.CharField(u'classificação', max_length=100, choices=classificação_CHOICES)
    assistido_no_cinema = models.BooleanField(blank=True, null=True)
    data_de_lançamento = models.DateField()

    #para retirar o "object" do titulo no django
    def __str__(self):
        return self.nome_do_filme
