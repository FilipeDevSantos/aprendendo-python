numeros = list()

while True:
    num = int(input('Digite um valor: '))
    if numeros.count(num) > 0:
        print('Valor duplicado! Não vou adicionar...')
    else:
        numeros.append(num)
        print('Valor adicionado com sucesso...')
    continuar = str(input('Quer continuar? [S/N] '))
    if continuar.lower() == 'n':
        break
print('-='*50)
numeros.sort()
print('Você digitou os valores {}'.format(numeros))