s = cont = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
    cont += 1
print('A soma dos {} valores foi {}'.format(cont, s))

