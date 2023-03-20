# funções

# def titulo(txt):
#     print('-' * 30)
#     print(txt)
#     print('-' * 30)
#
# # Programa Principal
# titulo('    CURSO EM VÍDEO      ')
# titulo('    PYTHON É MUITO BOM      ')
# titulo('    OI      ')

# def soma(a, b):
#     s = a + b
#     print(s)
#
#
# soma(4, 5)
# soma(8, 9)
# soma(b=2, a=1)

# def soma(a, b):
#     print(f'A = {a} e B = {b}')
#     s = a + b
#     print(f'A soma A + B = {s}')
#     print('-'*30)
#
#
# soma(2, 1)
# soma(b=2, a=1)

# def contador(* num):
#     print(num)
#     print(len(num))
#     print('-' * 30)
#
#
# contador(2, 7, 1)
# contador(8, 0)
# contador(4, 4, 7, 6, 2)

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)
