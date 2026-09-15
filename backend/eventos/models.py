from django.db import models
from palestrantes.models import Palestrante

class Evento(models.Model):
    titulo = models.CharField(max_length=200)
    data_evento = models.DateField()
    capacidade_maxima = models.IntegerField()
    ativo = models.BooleanField(default=True)
    
    # RELACIONAMENTO 1:N 
    # Justificativa: Um palestrante pode ministrar vários eventos ao longo do ano, 
    # mas cada evento específico desta listagem terá apenas um palestrante principal responsável.
    palestrante = models.ForeignKey(Palestrante, on_delete=models.CASCADE, related_name='eventos')

    def __str__(self):
        return self.titulo
