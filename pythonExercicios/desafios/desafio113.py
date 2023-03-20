def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO: por favor, digite um número inteiro válido\033[m')
            continue
        except KeyboardInterrupt:
            print('Entrada de dados interrompida pelo usuário.')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
           r = float(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO: por favor, digite um número inteiro válido\033[m')
            continue
        except KeyboardInterrupt:
            print('Entrada de dados interrompida pelo usuário.')
            return 0
        else:
            return r


n = leiaInt('Digite um número Inteiro: ')
r = leiaFloat('Digite um número real: ')
print(f'O valor inteiro foi {n} e o real foi {r}')
