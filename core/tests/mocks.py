import random

from core import models


nomes = [
    'Lorenzo Giovanni Vinicius Lopes',
    'Olivia Vitória Elza Mendes',
    'Analu Cecília Sabrina Pinto',
    'Edson Davi Freitas',
    'Priscila Milena Oliveira',
    'Sérgio Eduardo César Almada',
    'Agatha Brenda da Mata',
    'Raul Edson Vitor Dias',
    'Lúcia Isabelle Marli Assunção',
    'Henry Giovanni Drumond'
]

provedores_de_email = [
    '@gmail.com',
    '@hotmail.com',
    '@yahoo.com.br',
    '@bol.com',
    '@outlook.com.br'
]

cidades = [
    'Vassouras, RJ',
    'Curitiba, PA',
    'São Paulo, SP',
    'Rio de Janeiro, RJ',
    'Niterói, RJ'
]


def gerar_email(nome):
    nomes = list(map(lambda n: n.lower(), nome.split()))
    primeiro_nome, ultimo_nome = nomes[0], nomes[-1]
    email = random.choice(provedores_de_email)
    return ''.join([primeiro_nome, ultimo_nome, email])


def gerar_telefone(is_celular=False):
    ddd = random.randint(11, 60)
    primeira_parte = random.randint(80000, 99999) if is_celular else random.randint(3000, 5000)
    segunda_parte = random.randint(3000, 5000)
    return f'({ddd}) {primeira_parte}-{segunda_parte}'


def gerar_pessoas():
    for nome in nomes:
        pessoa = {
            'nome': nome,
            'telefone': gerar_telefone(),
            'celular': gerar_telefone(is_celular=True),
            'email': gerar_email(nome),
            'endereco': random.choice(cidades)
        }
        models.Contato.objects.create(**pessoa)
        print(f'Contato: {nome} criado com sucesso!')


if __name__ == '__main__':
    gerar_pessoas()
