num1 = int(input('Digite o 1º valor: '))
num2 = int(input('Digite o 2º valor: '))
num3 = int(input('Digite o 3º valor: '))
num4 = int(input('Digite o 4º valor: '))
tupla = (num1, num2, num3, num4)

c = 0
for num in tupla:
    if num == 9:
        c += 1
print(f'O número 9 apareceu {c} vezes.')
if tupla.count(3):
    print(f'O número 3 apareceu pela primeira vez na {tupla.index(3) + 1}º posição.')
else:
    print('Não tivemos número 3 na tupla.')
print(f'Os números pares que apareceram foram: ', end='')
for num in tupla:
    if num % 2 == 0:
        print(f' {num}', end='')
print('.')