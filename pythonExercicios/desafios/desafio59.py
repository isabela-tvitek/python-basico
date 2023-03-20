n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))

opcao = 0
while opcao != 5:
    print('''Opções:
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opcao = int(input('>>>>>>> Qual é a sua opção? '))
    #  -----------------------
    print('-=-' * 20)
    if opcao == 1:
        print('A soma entre {} + {} é {}'.format(n1, n2, n1+n2))
    elif opcao == 2:
        print('A multiplicação entre {} X {} é {}'.format(n1, n2, n1 * n2))
    elif opcao == 3:
        if n1 > n2:
            print('O maior entre {} e {} é {}'.format(n1, n2, n1))
        elif n2 > n1:
            print('O maior entre {} e {} é {}'.format(n1, n2, n2))
        else:
            print('São iguais')
    elif opcao == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção invalida')
        opcao = int(input('>>>>>>> Qual é a sua opção? '))
    print('-=-'*20)
print('Bye Bye, see you')
