n = str(input("Qual é seu nome completo? ")).strip()
nome = n.split()
pn = nome
un = nome[len(nome)-1]

print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}.'.format(pn[0]))
print('Seu último nome é {}.'.format(un))
