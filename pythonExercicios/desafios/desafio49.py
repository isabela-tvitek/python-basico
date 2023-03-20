n = int(input('Digite um número para ver sua tabuada: '))

for t in range(1, 11):
    m = n * t
    print('{} X {:2} = {:2}'.format(n, t, m))
