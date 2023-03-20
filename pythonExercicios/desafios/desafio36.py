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

valor = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))

pm = valor / (anos * 12)
print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}.'.format(valor, anos, pm))

s = salario * (30/100)

if pm < s:
    print('Empréstimo {}CONCEDIDO{}!'.format(cores['verde'], cores['limpa']))
else:
    print('Empréstimo {}NEGADO{}!'.format(cores['vermelho'], cores['limpa']))

