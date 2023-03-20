salario = float(input('Qual é o salário do funcionário? R$'))

novoSalario = salario + (salario * (15/100)) if salario <= 1250 else salario + (salario * (10/100))
# if salario <= 1250:
#     novoSalario = salario + (salario * (15/100))
# else:
#     novoSalario = salario + (salario * (10 / 100))

print('Quem ganhava R${:.2f} passa a ganhar R${:.2f}'.format(salario, novoSalario))
