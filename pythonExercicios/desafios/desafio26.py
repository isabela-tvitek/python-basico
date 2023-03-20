frase = str(input("Digite uma frase: ")).lower().strip()
ca = frase.count('a')
pa = frase.find('a')
ua = frase.rfind('a')

print('Analisando ...')
print('A letra A apareceu {} vezes na frase.'.format(ca))
print('A primeira letra A apareceu na posição {}.'.format(pa + 1))
print('A última letra A apareceu na posição {}.'.format(ua + 1))
