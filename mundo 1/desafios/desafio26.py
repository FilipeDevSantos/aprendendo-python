frase = str(input('Digite uma frase: '))

quantidade_A = frase.upper().count('A')
primeiro_A = frase.upper().find('A')
ultimo_A = frase.upper().rfind('A')

print(f'A frase têm {quantidade_A} letras "A".')
print(f'O primeiro "A" apareceu na posição {primeiro_A}.')
print(f'O ultimo "A" apareceu na posição {ultimo_A}.')