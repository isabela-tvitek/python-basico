# listas[]
# são mutaveis

# - list.append(x): Adiciona um item ao fim da lista.
# - list.insert(i, x): Insere um item em uma dada posição i.
# - del(): Deleta um elemento da lista ou a própria lista.
# - list.pop(i): Remove o item de posição i da lista e o retorna. Caso i não seja especificado, retorna o último elemento da lista.
# - list.remove(x): Remove o primeiro elemento, cujo valor seja x.
# - list.clear(): Remove todos os elementos da lista.
# - list.index(x[, start[, end]]): Retorna o índice do primeiro elemento cujo valor seja x.
# - list.count(x): Retorna o número de vezes que o valor x aparece na lista.
# - list.sort(key=None, reverse=False): Ordena os items da lista (os argumentos podem ser usados para customizar a ordenação).
# - list.reverse(): Reverte os elementos da lista.
# - list.copy(): Retorna uma lista com a cópia dos elementos da lista de origem.

# num = [2, 5, 9, 1]
# num[2] = 3
# num.append(7)
# num.insert(2, 2)
# num.sort()
# num.sort(reverse=True)
# print(len(num))
# num.pop()
# num.pop(2)
# num.remove(2)
# if 4 in num:
#     num.remove(4)
# else:
#     print('Valor não esta na lista')
# print(num)

# valores = list()
# valores = []
# valores.append(5)
# valores.append(9)
# valores.append(4)
# for cont in range(0, 5):
#     valores.append(int(input('Digite um valor: ')))
# for c, v in enumerate(valores):
#     print(f'Na posição {c} tem o valor {v}!')
# print('Fim')

a = [2, 3, 4, 7]
b = a
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
