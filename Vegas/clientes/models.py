from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255, blank=True)
    telefone = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255, blank=True)
    bairro = models.CharField(max_length=255, blank=True)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.nome

