numero = int(input('Digite um número: '))
somatorio = numero

c = 0
while 999 != numero:
    numero = int(input('Digite um número: '))
    c += 1
    if numero != 999:
        somatorio += numero
print(f'Você digitou {c} números e a soma entre eles foi {somatorio}.')