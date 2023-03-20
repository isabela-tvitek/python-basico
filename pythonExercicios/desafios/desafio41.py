from datetime import date
cores = {
    'limpa': '\033[m',
    'preto': '\033[30m',
    'vermelho': '\033[31m',
    'verde': '\033[32m',
    'amarelo': '\033[33m',
    'azul': '\033[34m',
    'magenta': '\033[35m',
    'ciano': '\033[36m',
    'cinza': '\033[37m',
    'branco': '\033[97m',
    'pretoebranco': '\033[0:97:40m',
    'brancoepreto': '\033[7:97m'
}

ano = int(input('Ano de nascimento: '))
hoje = date.today().year
idade = hoje - ano
print('O atleta tem {} anos'.format(idade))

if idade <= 9:
    print('Classificação: {}MIRIM{}'.format(cores['azul'], cores['limpa']))
elif idade <= 14:
    print('Classificação: {}INFANTIL{}'.format(cores['magenta'], cores['limpa']))
elif idade <= 19:
    print('Classificação: {}JUNIOR{}'.format(cores['verde'], cores['limpa']))
elif idade <= 25:
    print('Classificação: {}SÊNIOR{}'.format(cores['amarelo'], cores['limpa']))
else:
    print('Classificação: {}MASTER{}'.format(cores['ciano'], cores['limpa']))
