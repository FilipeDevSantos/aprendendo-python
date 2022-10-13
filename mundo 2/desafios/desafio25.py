numero = int(input('Digite um número: '))
fatorial = 1
print(f'\033[31m{numero}!\033[m =', end='')
while numero != 0:
    if numero != 1:
        print(f' \033[33m{numero} x', end='')
    else:
        print(f' \033[33m{numero}\033[m', end='')
    fatorial *= numero
    numero -= 1
print(f' = \033[32m{fatorial}\033[m.')