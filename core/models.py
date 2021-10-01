from django.db import models
from django.urls import reverse


class Contato(models.Model):
    nome = models.CharField('Nome', max_length=255)
    telefone = models.CharField('Telefone', max_length=20, blank=True, null=True)
    celular = models.CharField('Celular', max_length=20, blank=True, null=True)
    email = models.EmailField('E-mail', max_length=100, blank=True, null=True)
    endereco = models.CharField('Endereço', max_length=255, blank=True, null=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

    def excluir(self):
        self.ativo = False
        self.save()

    def get_absolute_url(self):
        return reverse('editar_contato', args=[self.id])
