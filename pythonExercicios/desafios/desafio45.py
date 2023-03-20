from random import randint
from time import sleep

print(''' Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA ''')

itens = ('PEDRA', 'PAPEL', 'TESOURA')
c = randint(0, 2)
j = int(input('Qual é a sua jogada? '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print('-=-'*10)
print('O computador escolheu {}'.format(itens[c]))
print('O jogador escolheu {}'.format(itens[j]))
print('-=-'*10)

if c == 0 and j == 1 or c == 1 and j == 2 or c == 2 and j == 0:
    print('O JOGADOR VENCE')
elif j == 0 and c == 1 or j == 1 and c == 2 or j == 2 and c == 0:
    print('O COMPUTADOR VENCE')
elif j == c:
    print('EMPATE')
else:
    print('JOGADA INVALIDA')

# if c == 0:
#     if j == 0:
#         print('EMPATE')
#     elif j == 1:
#         print('O JOGADOR VENCE')
#     elif j == 2:
#         print('O COMPUTADOR VENCE')
#     else:
#         print('JOGADA INVALIDA')
# elif c == 1:
#     if j == 0:
#         print('O COMPUTADOR VENCE')
#     elif j == 1:
#         print('EMPATE')
#     elif j == 2:
#         print('O JOGADOR VENCE')
#     else:
#         print('JOGADA INVALIDA')
# elif c == 2:
#     if j == 0:
#         print('O JOGADOR VENCE')
#     elif j == 1:
#         print('O COMPUTADOR VENCE')
#     elif j == 2:
#         print('EMPATE')
#     else:
#        print('JOGADA INVALIDA')
