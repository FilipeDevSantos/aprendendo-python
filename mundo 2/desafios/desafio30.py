media = maior = menor = somatorio = c = 0
continuar = ''

while continuar != 'N':
    numero = int(input('\nDigite um número: '))
    c += 1
    somatorio += numero
    if menor == 0:
        menor = numero
    elif numero > maior:
        maior = numero
    elif numero < menor:
        menor = numero
    continuar = str(input('''Ainda quer continuar a digitar números?
Caso não, digite [N]
continuar: ''').upper())

media = somatorio / c
print(f'A média dos números digitados é {media:.2f}, o maior número foi {maior} e o menor foi {menor}.')