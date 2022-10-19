def area(l, c):
    a = l*c
    print(f'A área do seu terreno de {l}x{c} é de {a}m².')

print('  Controle de Terrenos')
print('-'*25)
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
area(largura, comprimento)