d = float(input('Qual é a distância da sua viagem? '))

print('Você está prestes a começar uma viagem de {}Km.'.format(d))
'''
if d <= 200:
    valor = d * 0.50
else:
    valor = d * 0.45
'''
valor = d * 0.50 if d <= 200 else d * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(valor))
