matriz = [[], [], []]
linha = coluna = 0
for c in range(0, 9):
    num = int(input(f'Digite um valor para [{linha}, {coluna}] '))
    if coluna < 2:
        coluna += 1
        matriz[linha].append(num)
    else:
        matriz[linha].append(num)
        coluna = 0
        linha += 1
print('-='*50)
for linha in matriz:
    print('[{:^5}] [{:^5}] [{:^5}]'.format(linha[0], linha[1], linha[2]))