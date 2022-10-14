from random import randint

num1 = randint(0, 100)
num2 = randint(0, 100)
num3 = randint(0, 100)
num4 = randint(0, 100)
num5 = randint(0, 100)

tupla = (num1, num2, num3, num4, num5)
print(tupla)
tupla = sorted(tupla)
print(f'O maior valor é {tupla[0]}.')
print(f'O menor valor é {tupla[-1]}.')