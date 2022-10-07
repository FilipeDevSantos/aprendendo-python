numero = int(input('Digite um número: '))

print(f'unidade: {numero // 1 % 10:.0f}')
print(f'dezena: {numero // 10 % 10:.0f}')
print(f'centena: {numero // 100 % 10:.0f}')
print(f'milhar: {numero // 1000 % 10:.0f}')