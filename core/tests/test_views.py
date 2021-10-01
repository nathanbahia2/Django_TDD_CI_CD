from django.test import TestCase
from django.urls import reverse
from model_bakery import baker

from core.models import Contato


class TestIndexView(TestCase):
    def setUp(self):
        self.contatos = baker.make(Contato, 10)
        self.response = self.client.get(reverse('index'))

    def test_status_response(self):
        self.assertEqual(200, self.response.status_code)

    def test_context_deve_conter_elemento_contatos(self):
        context = self.response.context
        self.assertIn('contatos', context)

    def test_template_usado(self):
        self.assertTemplateUsed(self.response, 'core/index.html')

    def test_template_deve_conter_link_para_cadastrar_novo_contato(self):
        self.assertContains(self.response, '<a href="/cadastrar"')

    def test_template_deve_conter_link_para_editar_contatos(self):
        self.assertContains(self.response, self.contatos[0].get_absolute_url())


class TestEditarContatoView(TestCase):
    def setUp(self):
        self.contato = baker.make(Contato)

    def test_status_deve_ser_200_quando_contato_e_encontrado(self):
        response = self.client.get(reverse('editar_contato', args=[self.contato.id]))
        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, 'core/cadastro.html')

    def test_status_deve_ser_404_quando_contato_nao_e_encontrado(self):
        response = self.client.get(reverse('editar_contato', args=[999]))
        self.assertEqual(404, response.status_code)

    def test_post_valido_deve_alterar_contato(self):
        data = {
            'nome': 'Nathan',
            'endereco': 'Rio de Janeiro, RJ'
        }
        response = self.client.post(
            reverse('editar_contato', args=[self.contato.id]),
            data=data
        )

        contato = Contato.objects.first()
        self.assertEqual(data['nome'], contato. nome)
        self.assertEqual(data['endereco'], contato.endereco)
        self.assertRedirects(response, reverse('index'))

    def test_post_invalido_nao_deve_alterar_contato(self):
        data = {
            'email': 'emailInvalido',
        }
        response = self.client.post(
            reverse('editar_contato', args=[self.contato.id]),
            data=data
        )

        contato = Contato.objects.first()
        self.assertNotEqual(data['email'], contato.email)
        self.assertRedirects(response, reverse('index'))


class TestCadastrarContatoView(TestCase):
    def setUp(self):
        self.response = self.client.get(reverse('cadastrar_contato'))

    def test_status_response(self):
        self.assertEqual(200, self.response.status_code)

    def test_template_usado(self):
        self.assertTemplateUsed(self.response, 'core/cadastro.html')

    def test_post_valido_deve_criar_contato(self):
        data = {
            'nome': 'Nathan',
            'telefone': '(24) 3353-4567',
            'celular': '(24) 99999-1234',
            'email': '',
            'endereco': 'Vassouras, RJ'
        }
        self.client.post(
            reverse('cadastrar_contato'),
            data=data
        )
        contato = Contato.objects.first()
        self.assertEqual(data['nome'], contato.nome)
        self.assertEqual(data['telefone'], contato.telefone)
        self.assertEqual(data['celular'], contato.celular)
        self.assertEqual(data['endereco'], contato.endereco)
        self.assertIsNone(contato.email)

    def test_post_invalido_nao_deve_criar_contato(self):
        data = {
            'nome': '',
            'telefone': '(24) 3353-4567',
            'celular': '(24) 99999-1234',
            'email': 'nathan@datatype.com.br',
            'endereco': 'Vassouras, RJ'
        }
        self.client.post(
            reverse('cadastrar_contato'),
            data=data
        )
        self.assertEqual(0, Contato.objects.count())


class TestExcluirContatoView(TestCase):
    def setUp(self):
        self.contato = baker.make(Contato)
        self.response = self.client.get(reverse('excluir_contato', args=[self.contato.id]))

    def test_status_response(self):
        self.assertEqual(302, self.response.status_code)

    def test_deve_redirecionar_para_index_apos_exclusao(self):
        self.assertRedirects(self.response, reverse('index'))

    def test_contato_deve_ser_excluido_apos_request(self):
        contato = Contato.objects.first()
        self.assertFalse(contato.ativo)

    def test_status_deve_ser_404_quando_contato_nao_e_encontrado(self):
        response_invalida = self.client.get(reverse('excluir_contato', args=[999]))
        self.assertEqual(404, response_invalida.status_code)
