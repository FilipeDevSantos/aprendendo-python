numero = int(input('Digite um número: '))

total = 0
for c in range(1, numero + 1):
    if numero % c == 0:
        print('\033[33m', end='')
        total += 1
    else:
        print('\033[31m', end='')
    print(f'{c} ', end='')
print(f'\033[m\nO número {numero} foi dividido {total} de vezes.')
print('Logo esse número ', end='')
if total == 2:
    print('é primo!')
else:
    print('não é primo!')