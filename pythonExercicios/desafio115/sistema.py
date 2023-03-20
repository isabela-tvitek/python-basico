from desafio115.lib.interface import *
from desafio115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arqExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])

    if resposta == 1:
    # listagem o conteúdo de um arquivo.
        lerArquivo(arq)
    elif resposta == 2:
    # cadastrar uma nova pessoa.
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[0;31mERRO: por favor, digite um número inteiro válido\033[m')

