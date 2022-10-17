jogador = dict()
gols = list()
total = 0

jogador['nome'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))
for c in range(0, partidas):
    gols.append(int(input(f'Quantos gols na partida {c+1}: ')))
    total += gols[c]
jogador['total'] = total
jogador['gols'] = gols

print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for c in range(0, len(jogador["gols"])):
    print(f'    => Na partida {c+1}, fez {jogador["gols"][c]} gols.')
print(f'Foi um total de {jogador["total"]} gols.')