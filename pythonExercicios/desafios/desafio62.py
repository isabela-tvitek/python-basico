print('Gerador de PA')
print('-=-=-=-==-=-=-=-=-=-=-')
pt = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))

termo = pt
cont = 1
total = 0
mais = 10

while mais != 0:
    total = total + mais
    while cont <= total:
        print('{}'.format(termo), end=' -> ')
        termo += r
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais?: '))
print('FIM')
print('Progressão finalizada com {} termos mostrados'.format(total))
