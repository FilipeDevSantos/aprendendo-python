from random import randint
from time import sleep

numeros = list()

def sortear():
    print(f'Sorteando {len(numeros)} valores da lista: ', end='')
    for c in range(0, 5):
        numero = randint(0, 10)
        print(f' {numero}', end='', flush=True)
        sleep(0.2)
        numeros.append(numero)
    print(' PRONTO!')

def somarPar():
    total = 0
    for c in range(0, len(numeros)):
        if numeros[c] % 2 == 0:
            total += numeros[c]
    print(f'Somando os valores pares de {numeros}, temos {total}.')

sortear()
somarPar()