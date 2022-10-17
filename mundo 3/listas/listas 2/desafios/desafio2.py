numeros_organizados = [[], []]

for c in range(0, 7):
    valor = int(input('Digite um valor: '))

    if valor % 2 == 0:
        numeros_organizados[0].append(valor)
    else:
        numeros_organizados[1].append(valor)
numeros_organizados[0].sort()
numeros_organizados[1].sort()
print('-='*50)
print(f'Todos os números pares são {numeros_organizados[0]}')
print(f'Todos os números ímpares são {numeros_organizados[1]}')