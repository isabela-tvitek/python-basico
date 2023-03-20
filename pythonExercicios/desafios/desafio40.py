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

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

m = (n1 + n2)/2
print('Tirando {:.1f} e  {:.1f}, a média do aluno é {:.1f}'.format(n1, n2, m))

if m >= 7:
    print('O aluno está {}APROVADO{}!'.format(cores['verde'], cores['limpa']))
elif 5 <= m < 7:
    print('O aluno está {}EM RECUPERAÇÃO{}!'.format(cores['amarelo'], cores['limpa']))
elif m < 5:
    print('O aluno está {}REPROVADO{}!'.format(cores['vermelho'], cores['limpa']))
