from random import randint
from time import sleep

jogo_completo = list()
jogo = list()
print('-'*50)
print('{:^50}'.format('JOGO NA MEGA SENA'))
print('-'*50)
quantidade = int(input('Quantos jogos você quer que eu sortei? '))

for c in range(0, quantidade):
    for c in range(0, 6):
        jogada = randint(1, 60)
        while jogo.count(jogada) != 0:
            jogada = randint(1, 60)
        jogo.append(jogada)
    jogo.sort()
    jogo_completo.append(jogo[:])
    jogo.clear()
print('-='*5, f' SORTEANDO {quantidade} JOGOS ', '-='*5)
for i, palpite in enumerate(jogo_completo):
    print(f'Jogo {i+1}: {palpite}')
    sleep(1)
print('-='*5, ' < BOA SORTE! > ', '-='*5)