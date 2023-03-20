numeros = [[], []]

for n in range(0, 7):
    num = int(input(f'Digite o {n+1}° valor: '))
    if num % 2 == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)

numeros[0].sort()
print(f'Os valores pares são: {numeros[0]}')
numeros[1].sort()
print(f'Os valores impares são: {numeros[1]}')
