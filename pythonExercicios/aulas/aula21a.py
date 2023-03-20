# funçoes/2

# help(print())
# print(input.__doc__)

# def contador(i, f, p):
#     """
#     ->Faz uma contagem e mostra na tela.
#     :param i: inicio da contagem
#     :param f: fim da contagem
#     :param p: passo da contagem
#     :return: sem retorno
#     """
#     c = i
#     while c <= f:
#         print(f'{c }', end=' ')
#         c += p
#     print('FIM!')
#
#
# # contador(0, 100, 10)
# help(contador)

# def somar(a=0, b=0, c=0):
#    s = a + b + c
#    print(f'a soma é {s}')
#
#
# somar()
# somar(1)
# somar(2, 2)
# somar(3, 3, 3)

# def teste():
#    x = 8
#    print(f'Na função teste, n vale {n}')
#    print(f'Na função teste, x vale {x}')
#
#
# n = 2
# print(f'No programa principal, n vale {n}')
# teste()
# # print(f'No programa principal, x vale {x}')

# def funcao():
#    n1 = 8
#    print(f'N1 dentro vale {n1}')
#
#
# n1 = 2
# print(f'N1 fora vale {n1}')
# funcao()

# def somar(a=0, b=0, c=0):
#    s = a + b + c
#    return  s
#
#
# r1 = somar(3, 2, 5)
# r2 = somar(2, 5)
# print(f'{r1} e {r2}')

# def fatorial(num=1):
#     f = 1
#     for c in range(num, 0, -1):
#         f *= c
#     return  f
#
#
# n = int(input('Digite um número: '))
# print(f'O fatorial de {n} é igual a {fatorial(n)}')
# f1 = fatorial(5)
# f2 = fatorial(4)
# f3 = fatorial()
# print(f'Os resultados sao {f1}, {f2} e {f3}')
