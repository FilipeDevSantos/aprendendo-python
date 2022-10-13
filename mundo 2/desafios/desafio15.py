somatorio = 0
quantidade = 0
for c in range(1, 7):
    numero = int(input(f'Informe o {c}º número: '))
    if numero % 2 == 0:
        somatorio += numero
        quantidade += 1
print(f'O somatório de todos os {quantidade} valores pares é {somatorio}.')