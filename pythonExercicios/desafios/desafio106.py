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
bg = {
    'limpa': '\033[m',
    'preto': '\033[40m',
    'vermelho': '\033[41m',
    'verde': '\033[42m',
    'amarelo': '\033[43m',
    'azul': '\033[44m',
    'magenta': '\033[45m',
    'ciano': '\033[46m',
    'cinza': '\033[47m',
    'branco': '\033[107m',
}

#  minha solução
while True:
    def ajuda(txt):
        print('~' * 30)
        print(f'{bg["magenta"]}{cores["branco"]}Acessando o manual do comando {txt}{cores["limpa"]}{bg["limpa"]}')
        print('~' * 30)
        return help(f'{txt}')


    print('~'*30)
    print(f'{bg["ciano"]}{cores["preto"]} SISTEMA DE AJUDA PYHELP {cores["limpa"]}{bg["limpa"]}')
    print('~'*30)

    opc = str(input('Função ou Biblioteca: ')).lower()

    if opc != 'fim':
        print(ajuda(opc))
    else:
        break

# -------------------------------------------------------------------------------------------------------------

# # solução curso
# c = ('\033[m'           # 0 - sem cor
#      '\033[0;30;41m'    # 1 - vermelho
#     )
# def ajuda(comando):
#     help(comando)
#
# def titulo(msg, cor=0):
#     tam = len(msg)+4
#     print('~'*tam)
#     print(msg)
#     print('~'*tam)
#
# opc = ''
# while True:
#     titulo('  SISTEMA DE AJUDA PyHELP', 1)
#     opc = str(input('Função ou Biblioteca: ')).lower()
#     if opc != 'fim':
#         ajuda(opc)
#     else:
#         break
#
# titulo('  ATE LOGO!', 1)
