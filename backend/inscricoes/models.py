from django.db import models

class Inscricao(models.Model):
    nome_participante = models.CharField(max_length=150)
    email_participante = models.EmailField()
    data_inscricao = models.DateTimeField(auto_now_add=True)
    pago = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nome_participante} - {self.email_participante}"
