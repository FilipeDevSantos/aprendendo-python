def ficha(nome, gols):
    return f'O jogador {nome} fez {gols} gol(s) no campeonato.'


nome = str(input('Nome do jogador: '))
gols = str(input('Número de gols: '))

if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    print(ficha(nome='<desconhecido>', gols=gols))
else:
    print(ficha(nome=nome, gols=gols))