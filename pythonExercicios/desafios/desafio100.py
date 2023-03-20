from random import randint
from time import sleep

def sorteia(numeros):
    print('Sorteando 5 valores da lista: ', end='')
    for c in range(0, 5):
        n = randint(1, 10)
        numeros.append(n)
        print(n, end=' ')
        sleep(0.5)
    print('PRONTO!')

def somaPar(numeros):
    soma = 0
    for n in numeros:
        if n % 2 == 0:
            soma += n
    print(f'Somando os valores pares de {numeros}, temos {soma}')

numeros = list()
sorteia(numeros)
somaPar(numeros)

