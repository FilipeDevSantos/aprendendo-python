num = [2, 3, 4, 3]
num[3] = 8
print(num)
num.append(2)
print(num)
num.sort()
print(num)
num.sort(reverse=True)
print(num)
print(f'O tamanho da lista é {len(num)}.')
num.insert(2, 6)
print(num)
num.pop()
print(num)
if 3 in num:
    num.remove(3)
print(num)

valores = list()
for c in range(0, 5):
    numero = int(input('Digite um valor: '))
    valores.append(numero)

for i, v in enumerate(valores):
    print(f'Na posição {i} encontrei o valor {v}!')
print('Cheguei ao final da lista.')