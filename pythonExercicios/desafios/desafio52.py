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

num = int(input('Digite um número: '))
cont = 0
for n in range(1, num+1):
    p = num % n
    if p == 0:
        print('{}{}{} '.format(cores['amarelo'], n, cores['limpa']), end='')
        cont += 1
    else:
        print('{}{}{} '.format(cores['vermelho'], n, cores['limpa']), end='')
print('\nO número {} foi divisível {} vezes'.format(num, cont))

if cont == 2:
    print('E por isso ele É PRIMO')
else:
    print('E por isso ele NÃO É PRIMO')
