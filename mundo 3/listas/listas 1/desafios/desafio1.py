numeros = list()
menores = list()
maiores = list()

for c in range(0, 5):
    num = int(input('Digite um número: '))
    numeros.append(num)

maior = menor = 0
menor = numeros[0]

for num in numeros:
    if num > maior:
        maior = num
    if num < menor:
        menor = num

for i, v in enumerate(numeros):
    if v == maior:
        maiores.append(i)
    if v == menor:
        menores.append(i)
print('-='*50)
print(f'O maior valor digitado foi {maior} nas posições', end='')
for valor in maiores:
    print(f' {valor}...', end='')
print(f'\nO menor valor digitado foi {menor} nas posições', end='')
for valor in menores:
    print(f' {valor}...', end='')