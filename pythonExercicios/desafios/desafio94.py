dado = dict()
pessoas = list()
soma = media = 0
while True:
    dado['nome'] = str(input('Nome: '))
    while True:
        dado['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if dado['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    dado['idade'] = int(input('Idade: '))
    soma += dado['idade']
    pessoas.append(dado.copy())
    # ---------------------------------------------
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if opcao == 'N':
        break
# ---------------------------------------------
print('-=-'*30)
print(f'- O grupo tem {len(pessoas)} pessoas.')

media = soma / len(pessoas)
print(f'- A média de idade é de {media:5.2f} anos.')

print(f'- As mulheres cadastradas foram: ', end='')
for p in pessoas:
    if p['sexo'] in 'Ff':
        print(p['nome'], end=' ')
print()

print(f'- Lista das pessoas que estão acima da média: ')
for p in pessoas:
    if p['idade'] >= media:
        print(f'\n{p["nome"]}; {p["sexo"]}; {p["idade"]};')
print('<< ENCERRADO >>')
