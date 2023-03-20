valores = list()
pares = list()
impares = list()

while True:
    valores.append(int(input('Digite um valor: ')))
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if opcao == 'N':
        break

for v in range(0, len(valores)):
    if valores[v] % 2 == 0:
        pares.append(valores[v])
    else:
        impares.append(valores[v])

print('-=-' * 30)
print(f'Foram digitados os valores: {valores}')
print(f'Os valores PARES são: {pares}')
print(f'Os valores IMPARES são: {impares}')
