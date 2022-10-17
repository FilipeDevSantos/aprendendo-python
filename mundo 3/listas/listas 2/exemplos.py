galera = list()
dados = list()
totmai = totmen = 0

for c in range(0, 3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    galera.append(dados[:])
    dados.clear()

for pessoa in galera:
    if pessoa[1] >= 18:
        print(f'{pessoa[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{pessoa[0]} é menor de idade.')
        totmen += 1

print(f'Temos um total de {totmai} maiores e {totmen} menores de idade.')