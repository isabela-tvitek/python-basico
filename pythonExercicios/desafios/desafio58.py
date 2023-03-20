from random import randint
p = randint(0, 10)
print('Sou seu computador... \nAcabei de pensar em um número entre 0 e 10.')
print('Será que você consegue advinhar qual foi?')

acertou = False
palpites = 0
while not acertou:
    n = int(input("Qual é seu palpite? "))
    palpites += 1
    if n == p:
        acertou = True
    else:
        if n < p:
            print('Mais... Tente mais uma vez.')
        elif n > p:
            print('Menos... Tente mais uma vez.')
print('-'*20)
print('Acertou com {} tentativas. PARABÉNS!'.format(palpites))
