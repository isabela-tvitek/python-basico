print('-'*30)
print('CADASTRE UMA PESSOA')
print('-'*30)

cont = homem = mulher = 0
while True:
    idade = int(input('Idade: '))
    # -------------------------------------------------------------------
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    # -------------------------------------------------------------------
    if idade > 18:
        cont += 1
    # ------------------
    if sexo == 'M':
        homem += 1
    # ------------------
    if sexo == 'F' and idade < 20:
        mulher += 1
    # -------------------------------------------------------------------
    opcao = ' '
    while opcao not in 'SN':
        print('-' * 30)
        opcao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        print('-' * 30)
    # -------------------------------------------------------------------
    if opcao == 'N':
        break
print('Total de pessoas com mais de 18 anos: {}'.format(cont))
print('Ao todo temos {} homens cadastrados'.format(homem))
print('E temos {} mulheres com menos de 20 anos'.format(mulher))
