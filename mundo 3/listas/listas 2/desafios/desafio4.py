matriz = [[], [], []]
somatorio = somatorio_terceira = maior_segunda = linha = coluna = 0
for c in range(0, 9):
    num = int(input(f'Digite um valor para [{linha}, {coluna}] '))
    if coluna < 2:
        coluna += 1
        matriz[linha].append(num)
        if num % 2 == 0:
            somatorio += num
    else:
        matriz[linha].append(num)
        if num % 2 == 0:
            somatorio += num
        coluna = 0
        linha += 1
print('-='*50)
for linha in matriz:
    print('[{:^5}] [{:^5}] [{:^5}]'.format(linha[0], linha[1], linha[2]))
for l in range(0, 3):
    somatorio_terceira += matriz[l][2]
for c in range(0, 3):
    if maior_segunda < matriz[1][c]:
        maior_segunda = matriz[1][c]
print(f'\nA soma de todos os valores é {somatorio}.')
print(f'A soma dos valores da terceira coluna é {somatorio_terceira}.')
print(f'O maior valor da segunda coluna é {maior_segunda}.')