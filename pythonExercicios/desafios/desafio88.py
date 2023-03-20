from random import randint
from time import sleep
jogos = list()
sorteio = list()

print('-'*40)
print(f'{"JOGA NA MEGA SENA":^40}')
print('-'*40)
qtd = int(input('Quantos números quer que eu sorteie? '))

for n in range(0, qtd):
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in sorteio:
            sorteio.append(num)
            cont += 1
        if cont >= 6:
            break
    sorteio.sort()
    jogos.append(sorteio[:])
    sorteio.clear()

print(f'-=--=--=--=- SORTEANDO OS {qtd} JOGOS -=--=--=--=-')
for n in range(0, qtd):
    jogos.sort()
    print(f'Jogo {n+1}: {jogos[n]}')
    sleep(1)
print(f'-=--=--=--=--=- < BOA SORTE! > -=--=--=--=--=-')
