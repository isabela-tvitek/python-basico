soma = 0
media = 0
maisVelho = 0
maisVelhoNome = ''
totFem = 0
for p in range(1, 5):
    print('----- {}° PESSOA -----?'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()

    soma += idade
    # -------------------------------
    if p == 1 and sexo in 'Mm':
        maisVelho = idade
        maisVelhoNome = nome
    else:
        if sexo in 'Mm' and idade > maisVelho:
            maisVelho = idade
            maisVelhoNome = nome
    # -------------------------------
    if sexo in 'Ff':
        if idade < 20:
            totFem += 1
    # -------------------------------
media = soma/4

print('A média de idade do grupo é de {} anos'.format(media))
print('O homem mais  velho tem {} anos e se chama {}.'.format(maisVelho, maisVelhoNome))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(totFem))
