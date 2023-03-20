# dicionarios {} ou dict()
# pessoas = {'nome': 'Isabela', 'sexo': 'F', 'idade': 21}
# print(pessoas)
# print(pessoas['nome'])
# print(pessoas['idade'])
# print(pessoas)
# print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
# print(pessoas.keys())
# print(pessoas.values())
# print(pessoas.items())
# for k in pessoas.keys():
#     print(k)
# for k in pessoas.values():
#     print(k)
# for k, v in pessoas.items():
#     print(f'{k} = {v}')
#
# del pessoas['sexo']
# pessoas['nome'] = 'Ana'
# print(pessoas)
# pessoas['peso'] = 74.3
# --------------------------------------------------------------------------------
# brasil = []
# estado1 = {'uf': 'Rio de janeiro', 'sigla': 'RJ'}
# estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
# brasil.append(estado1)
# brasil.append(estado2)
# print(estado1)
# print(estado2)
# print(brasil)
# print(brasil[0])
# print(brasil[0]['uf'])
# --------------------------------------------------------------------------------
estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
print(brasil)
for e in brasil:
    for k, v in e.items():
        print(v)