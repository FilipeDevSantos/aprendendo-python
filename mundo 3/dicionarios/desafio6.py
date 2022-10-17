jogadores = list()
jogador = dict()
gols = list()
total = 0
while True:
    jogador['nome'] = str(input('Nome do Jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))
    for c in range(0, partidas):
        gols.append(int(input(f'Quantos gols na partida {c+1}: ')))
        total += gols[c]
    jogador['gols'] = gols.copy()
    jogador['total'] = total
    jogadores.append(jogador.copy())
    gols.clear()
    continuar = str(input('Quer continuar? [S/N] ').lower())
    if continuar == 'n':
        break
print('-='*30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-'*60)
for i, v in enumerate(jogadores):
    print(f'{i:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print()

while True:
    print('-'*60)
    cod = int(input('Mostrar dados de qual jogador? (usar 999 para parar) '))
    if cod == 999:
        break
    elif cod > len(jogadores)-1:
        print('ERRO! Não existe jogador com esse código! Tente novamente')
    else:
        print(f'-- Levantamento do JOGADOR {jogadores[cod]["nome"]}')
        for c in range(0, len(jogadores[cod]["gols"])):
            print(f'  Na partida {c+1}, fez {jogadores[cod]["gols"][c]} gols.')
print('<< VOLTE SEMPRE >>')