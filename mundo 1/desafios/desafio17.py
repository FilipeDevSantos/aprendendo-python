from math import hypot

co = float(input('Informe o comprimento do cateto oposto: '))
ca = float(input('Informe o comprimento do cateto adjacente: '))

# h = ((co ** 2) + (ca ** 2)) ** 0.5
h = hypot(co, ca)

print(f'A hipotenusa é igual a {h:.2f}.')