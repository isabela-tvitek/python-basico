from random import randint

print('-='*30)
print('VAMOS JOGAR PAR OU IMPAR')
print('-='*30)
cont = 0
while True:
    n = int(input('Diga um valor: '))
    c = randint(0, 10)
    s = c + n
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('PAR ou IMPAR? [P/I]')).strip().upper()[0]
    print('Você jogou {} e o computador {}. Total de {} '.format(n, c, s), end='')
    print('DEU PAR' if s % 2 == 0 else 'DEU IMPAR')

    if tipo == 'P':
        if s % 2 == 0:
            cont += 1
            print('Você VENCEU!')
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if s % 2 == 0:
            print('Você PERDEU!')
            break
        else:
            cont += 1
            print('Você VENCEU!')
            print('-=' * 30)
    print('Vamos jogar novamente...')

print('-='*30)
print('GAME OVER! Você venceu {} vezes'.format(cont))
