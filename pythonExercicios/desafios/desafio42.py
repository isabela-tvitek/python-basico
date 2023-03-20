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

l1 = float(input('Primeiro segmento: '))
l2 = float(input('Segundo segmento: '))
l3 = float(input('Terceiro segmento: '))

isTriangulo = l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2

if isTriangulo:
    print('O segmentos acima {}PODEM FORMAR{} um triângulo '.format(cores['verde'], cores['limpa']), end='')

    if l1 == l2 == l3:
        print('{}EQUILÁTERO{}!'.format(cores['magenta'], cores['limpa']))
    elif l1 != l2 != l3 != l1:
        print('{}ESCALENO{}!'.format(cores['azul'], cores['limpa']))
    else:
        print('{}ISÓSCELES{}!'.format(cores['ciano'], cores['limpa']))
else:
    print('Os segmentos acima {}NÃO PODEM FORMAR{} um triângulo'.format(cores['vermelho'], cores['limpa']))


