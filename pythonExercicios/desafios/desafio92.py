from datetime import datetime

funcionario = dict()
funcionario['nome'] = str(input('Nome: '))
ano = int(input('Ano de nascimento: '))
funcionario['idade'] = datetime.now().year - ano
funcionario['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))

if funcionario['ctps'] != 0:
    funcionario['ano'] = int(input('Ano de contratação: '))
    funcionario['salario'] = float(input('Salário: R$'))
    funcionario['aposentadoria'] = funcionario['idade'] + ((funcionario['ano'] + 35) - datetime.now().year)

#  ---------------------------------------------------------------------------
for k, v in funcionario.items():
    print(f'{k} tem o valor {v}')
