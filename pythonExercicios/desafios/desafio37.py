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

num = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para conversão:')
print('[ 1 ] converter para BINÁRIO')
print('[ 2 ] converter para OCTAL')
print('[ 3 ] converter para HEXADECIMAL')

opcao = int(input('Sua opção: '))

if opcao == 1:
    print('{} convertido para {}BINÁRIO{} é igual a {}'.format(num, cores['verde'], cores['limpa'], bin(num)[2:]))
elif opcao == 2:
    print('{} convertido para {}OCTAL{} é igual a {}'.format(num, cores['ciano'], cores['limpa'], oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para {}HEXADECIMAL{} é igual a {}'.format(num, cores['magenta'], cores['limpa'], hex(num)[2:]))
else:
    print('{}Opção inválida{}! Tente novamente.'.format(cores['vermelho'], cores['limpa']))




