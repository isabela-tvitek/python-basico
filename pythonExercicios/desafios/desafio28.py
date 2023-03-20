from random import randint
from time import sleep
p = randint(0, 5)

print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'*20)

n = int(input("Em que número eu pensei? "))
print('PROCESSANDO...')
sleep(2)
if n == p:
    print('PARABÉNS! você conseguiu me vencer! eu pensei no número {}.'.format(p))
else:
    print('GANHEI! eu pensei no número {} e não no {}.'.format(p, n))
