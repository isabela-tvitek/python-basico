from datetime import date

hoje = date.today().year
maiores = 0
menores = 0
for i in range(1, 8):
    ano = int(input('Em que ano a {}° pessoa nasceu?'.format(i)))
    idade = hoje - ano

    if idade >= 21:
        maiores += 1
    else:
        menores += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(maiores))
print('Ao todo tivemos {} pessoas menores de idade'.format(menores))
