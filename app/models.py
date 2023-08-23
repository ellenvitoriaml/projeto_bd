from django.db import models

class Usuario(models.Model):
    cpf = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()

    def __str__(self):
        return self.nome