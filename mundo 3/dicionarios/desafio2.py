from random import randint
from time import sleep

jogadas = dict()
ranking = list()

jogadas['jogador1'] = randint(1, 6)
jogadas['jogador2'] = randint(1, 6)
jogadas['jogador3'] = randint(1, 6)
jogadas['jogador4'] = randint(1, 6)

print('Valores sorteados: ')
for k, v in jogadas.items():
    print(f'O jogador {k} tirou {v}')
    sleep(1)
print('-='*30)
print(' == RANKING DOS JOGADORES ==')
ranking = sorted(jogadas.items(), key=lambda item: item[1], reverse=True)
for i, v in enumerate(ranking):
    print(f'    {i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)