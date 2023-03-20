dado = list()
pessoas = list()
pesoMaior = pesoMenor = 0

while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    pessoas.append(dado[:])
    # ---------------------------------------------
    if len(pessoas) == 1:
        pesoMaior = dado[1]
        pesoMenor = dado[1]
    else:
        if dado[1] > pesoMaior:
            pesoMaior = dado[1]
        if dado[1] < pesoMenor:
            pesoMenor = dado[1]
    # ---------------------------------------------
    dado.clear()
    # ---------------------------------------------
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if opcao == 'N':
        break
# ---------------------------------------------
print('-=-'*30)
print(f'Ao todo, você cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso foi de {pesoMaior}. Peso de ', end='')
for p in pessoas:
    if p[1] == pesoMaior:
        print(f'[{p[0]}]', end=' ')

print(f'\nO menor peso foi de {pesoMenor}. Peso de ', end='')
for p in pessoas:
    if p[1] == pesoMenor:
        print(f'[{p[0]}]', end=' ')
