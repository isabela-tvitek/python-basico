#      st tx bg
# \033[0;33;44m
'''
---------------------------------------------------
   style        |     text       |   background   |
- 0  none       |- 30 preto      |- 40 preto      |
- 1 bold        |- 31 vermelho   |- 41 vermelho   |
- 4 underline   |- 32 verde      |- 42 verde      |
- 7 negative    |- 33 amarelo    |- 43 amarelo    |
                |- 34 azul       |- 44 azul       |
                |- 35 magenta    |- 45 magenta    |
                |- 36 ciano      |- 46 ciano      |
                |- 37 cinza      |- 47 cinza      |
                |- 97 branco     |- 107 branco    |
---------------------------------------------------
'''

print('\033[1;31;43mOlá, Mundo!\033[m')
print('\033[4;30;45mOlá, Mundo!\033[m')
print('\033[4;97;45mOlá, Mundo!\033[m')
print('\033[4;30;107mOlá, Mundo!\033[m')
print('\033[7;40mOlá, Mundo!\033[m')
a = 3
b = 5
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m!!!'.format(a, b))
nome = 'Isabela'
print('Olá! muito prazer em te conhecer {}{}{}!!!'.format('\033[4;34m', nome, '\033[m'))
nome = 'Isabela'
cores = {
    'limpa': '\033[m',
    'preto': '\033[30m',
    'vermelho': '\033[31m',
    'verde': '\033[32m',
    'amarelo': '\033[33m',
    'azul': '\033[34m',
    'magenta': '\033[35m',
    'ciano': '\033[36m',
    'cinza': '\033[37m',
    'branco': '\033[97m',
    'pretoebranco': '\033[0:97:40m',
    'brancoepreto': '\033[7:97m'
}
print('Olá! muito prazer em te conhecer {}{}{}!!!'.format(cores['brancoepreto'], nome, cores['limpa']))
print('Olá! muito prazer em te conhecer {}{}{}!!!'.format(cores['pretoebranco'], nome, cores['limpa']))
