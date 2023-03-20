valores = list()
while True:
    n = int(input('Digite um valor: '))
    valores.append(n)
    print('Valor adicionado com sucesso...')

    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if opcao == 'N':
        break

print('-=-' * 30)
print(f'Foram digitados {len(valores)} valores')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são {valores}')
if 5 in valores:
    print(f'O número 5 faz parte da lista!')
else:
    print(f'O número 5 não faz parte da lista!')
