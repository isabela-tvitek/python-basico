frase = str(input('Digite uma frase: ')).strip().upper()

palavras = frase.split()
junto = ''.join(palavras)
# inverso = ''
# for letra in range(len(junto)-1, -1, -1):
#     inverso += junto[letra]

inverso = junto[::-1] #sem usar o for
print('frase: {}, inverso: {}'.format(junto, inverso))
if junto == inverso:
    print('Temos um PALÍNDROMO!')
else:
    print('A frase digitada NÃO É PALÍNDROMO!')
