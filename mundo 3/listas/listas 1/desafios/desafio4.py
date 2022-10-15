numeros = list()
while True:
    num = int(input('Digite um valor: '))
    numeros.append(num)
    continuar = str(input('Quer continuar? [S/N] '))
    if continuar == 'n':
        break
print(f'Você digitou {len(numeros)} elementos.')
numeros.sort(reverse=True)
print(f'Os valores em ordem decrescente são {numeros}')
if numeros.count(5) > 0:
    print('O valor 5 faz parte da lista e se encontra na posição {}!'.format(numeros.index(5)))
else:
    print('O valor 5 não faz parte da lista!')
