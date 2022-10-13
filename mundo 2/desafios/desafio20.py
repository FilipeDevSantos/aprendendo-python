peso_maior = 0
peso_menor = 0

for c in range(0, 5):
    peso = int(input('Digite o peso: '))
    if c == 0:
        peso_menor = peso
    elif peso < peso_menor:
        peso_menor = peso
    elif peso > peso_maior:
        peso_maior = peso
print(f'O maior peso foi {peso_maior} e o menor foi {peso_menor}.')