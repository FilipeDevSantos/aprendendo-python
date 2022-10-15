numeros = list()
pares = list()
impares = list()
while True:
    num = int(input('Digite um valor: '))
    numeros.append(num)
    continuar = str(input('Quer continuar? [S/N] '))
    if continuar == 'n':
        break
for num in numeros:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
print('-='*50)
print(f'A lista completa é {numeros}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')