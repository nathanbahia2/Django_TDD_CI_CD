from django.test import TestCase
from django.urls import reverse
from model_bakery import baker

from core.models import Contato


class TestContatoModel(TestCase):
    def setUp(self):
        self.contato = baker.make(Contato)

    def test_str_contato(self):
        self.assertEqual(self.contato.nome, str(self.contato))

    def test_excluir_contato(self):
        self.contato.excluir()
        self.assertFalse(self.contato.ativo)

    def test_get_absolute_url(self):
        self.assertEqual(
            reverse('editar_contato', args=[self.contato.id]),
            self.contato.get_absolute_url()
        )
