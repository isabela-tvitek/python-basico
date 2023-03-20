# from time import sleep
# def contador(i, f, p):
#     print('-=' * 30)
#     if i < f:
#         print(f'Contagem de {i} até {f} de {p} em {p}')
#         for c in range(i, f, p):
#             print(c, end=' ')
#             sleep(0.5)
#         print('FIM!')
#     elif i > f:
#         if p < 0:
#             print(f'Contagem de {i} até {f} de {p * -1} em {p * -1}')
#             for c in range(i, f, p):
#                 print(c, end=' ')
#                 sleep(0.5)
#             print('FIM!')
#         elif p == 0:
#             print(f'Contagem de {i} até {f} de {1} em {1}')
#             for c in range(i, f):
#                 print(c, end=' ')
#                 sleep(0.5)
#             print('FIM!')
#         else:
#             for c in range(i, f, -p):
#                 print(c, end=' ')
#                 sleep(0.5)
#             print('FIM!')
#  contador(1, 10, 1)
#  contador(10, 0, -2)
# print('-=' * 30)
# i = int(input('Inicio: '))
# f = int(input('Fim: '))
# p = int(input('Passo: '))
# contador(i, f+1, p)

#  Solução curso
from time import sleep

def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('-=' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}')

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont -= p
        print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 30)
print('Agora é sua vez de personalizar a contagem!')
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f+1, p)
