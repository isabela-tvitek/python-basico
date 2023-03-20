from datetime import date
ano = int(input('Ano de nascimento: '))

hoje = date.today().year
idade = hoje - ano
print('Quem nasceu em {} tem {} anos em {}.'.format(ano, idade, hoje))

# diferenca = 18 - idade
# if idade < 18:
#     print('Ainda faltam {} ano(os) para seu alistamento'.format(diferenca))
#     print('Seu alistamento será em {}'.format(hoje+diferenca))
# elif idade > 18:
#     print('Você já deveria ter se alistado há {} ano(os)'.format(diferenca*-1))
#     print('Seu alistamento foi em {}'.format(hoje - (diferenca*-1)))
# else:
#     print('Você deve se alistar IMEDIATAMENTE!')

if idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} ano(os) para seu alistamento'.format(saldo))
    print('Seu alistamento será em {}'.format(hoje+saldo))
elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} ano(os)'.format(saldo))
    print('Seu alistamento foi em {}'.format(hoje - saldo))
else:
    print('Você deve se alistar IMEDIATAMENTE!')
