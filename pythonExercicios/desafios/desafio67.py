while True:
    print('-'*20)
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-'*20)

    if n < 0:
        break

    for t in range(1, 11):
        print('{:2} x {:2} = {:2}'.format(n, t, n*t))
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
