aluno = list()

pesoMaior = pesoMenor = cont = 0
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    aluno.append([nome, [nota1, nota2], media])

    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if opcao == 'N':
        break

print('-=-' * 30)
print(f'{"N°":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 40)

for i, a in enumerate(aluno):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')

while True:
    print('-' * 40)
    opcao = int(input('Mostrar notas de qual aluno? (999 interrompe): '))

    if opcao == 999:
        break
    if opcao <= len(aluno) -1:
        print(f'Notas de {aluno[opcao][0]} são {aluno[opcao][1]}')
print('<<< VOLTE SEMPRE >>>')
