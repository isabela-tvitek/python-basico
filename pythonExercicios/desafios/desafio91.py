from random import randint
from time import sleep
from operator import itemgetter

# sorteio = dict()
# info = list()
# for c in range(1, 5):
#     sorteio['jogador'] = f'jogador{c}'
#     sorteio['dado'] = randint(1, 6)
#     info.append(sorteio.copy())
# print('Valores sorteados:')
# for v in info:
#     print(f'    O {v["jogador"]} tirou {v["dado"]}')
#     sleep(1)
# print('Ranking dos jogadores:')
# for i, v in enumerate(info):
#     print(f' {i+1}° lugar: {v["jogador"]} com {v["dado"]}')
#     sleep(1)

jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
ranking = list()

print('Valores sorteados:')
for k, v in jogo.items():
    print(f'    - {k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('Ranking dos jogadores:')
for i, v in enumerate(ranking):
    print(f'    - {i+1}° lugar: {v[0]} com {v[1]}.')
    sleep(1)
