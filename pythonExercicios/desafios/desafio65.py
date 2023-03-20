resposta = 'S'
cont = 0
soma = 0
maior = 0
menor = 0
while resposta in 'Ss':
    n = int(input('Digite um número: '))
    cont += 1
    soma += n
    resposta = str(input('Quer continuar? [S/N] ')).upper().strip()[0]

    if cont == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
#  ------------------------
media = soma/cont
print('Você digitou {} números e a média foi {}'.format(cont, media))
print('O maior foi {} e o menor foi {}'.format(maior, menor))
