exp = str(input('Digite a expressão: '))
pilha = []

for simb in exp:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print(f'Sua expressão está válida!')
else:
    print(f'Sua expressão está Errada!')
