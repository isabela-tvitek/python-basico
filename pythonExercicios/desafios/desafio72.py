extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
           'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    while True:
        n = int(input('Digite um número entre 0 e 20: '))
        if 0 <= n <= 20:
            break
        print('Tente novamente. ', end='')
    print(f'Você digitou o número {extenso[n]}')
    # -------------------------------------------------------------------
    opcao = ' '
    while opcao not in 'SN':
        print('-' * 30)
        opcao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        print('-' * 30)
    # -------------------------------------------------------------------

    if opcao == 'N':
        break
