from dataclasses import replace


frase = str(input('Digite uma frase sem acentos: ').upper())
frase = frase.replace(' ', '')

frase_reversa = ''
for letra in range(len(frase) -1, -1, -1):
    frase_reversa += frase[letra]
if frase == frase_reversa:
    print('É um palíndromo!')
else:
    print('Não é um palíndromo!')