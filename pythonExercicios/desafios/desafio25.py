nome = str(input("Qual é seu nome completo? ")).strip()
isExist = 'silva' in nome.lower()
print('Seu nome tem Silva? {}'.format(isExist))
