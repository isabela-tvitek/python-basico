valores = list()
for cont in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {cont}: ')))

print('-=-'*30)
print(f'Você digitou os valores {valores}')

print(f'O maior valor digitado foi {max(valores)} nas posições ', end='')
for pos, v in enumerate(valores):
    if max(valores) == v:
        print(pos, end='...')

print(f'\nO menor valor digitado foi {min(valores)} nas posições ', end='')
for pos, v in enumerate(valores):
    if min(valores) == v:
        print(pos, end='...')


