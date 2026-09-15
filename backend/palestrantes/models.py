from django.db import models

class Palestrante(models.Model):
    nome = models.CharField(max_length=100)
    biografia = models.TextField()
    instituicao = models.CharField(max_length=150)

    def __str__(self):
        return self.nome
