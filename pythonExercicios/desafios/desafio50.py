soma = 0
count = 0
for n in range(1, 7):
    num = int(input('Digite o {}° valor número: '.format(n)))
    p = num % 2
    if p == 0:
        soma += num
        count += 1
print('Você informou {} números PARES e a soma foi {}'.format(count, soma))
