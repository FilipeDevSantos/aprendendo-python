# estudando operadores e entendendo a ordem de precedência

soma = 5 + 2 == 7
sub = 5 - 2 == 3
mult = 5 * 2 == 10
div = 5 / 2 == 2.5
divint = 5 // 2 == 2
resdiv = 5 % 2 == 1

print(f'A soma está certa? {soma}')
print(f'A subtração está certa? {sub}')
print(f'A multiplicação está certa? {mult}')
print(f'A divisão está certa? {div}')
print(f'A divisão inteira está certa? {divint}')
print(f'O resto da divisão está certo? {resdiv}')

# ordem de precedência
# 1 -> ()
# 2 -> **
# 3 -> / * // %
# 4 -> + -

resultado = ((5 + 2 * 4 - (5 / 3) ** 4) // 3) % 2

print(f'O resultado dessa conta doida é: {resultado}')