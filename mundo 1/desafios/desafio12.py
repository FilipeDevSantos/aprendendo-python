altura = float(input('Digite a altura da parede: '))
largura = float((input('Digite a largura da parede: ')))

area = altura * largura
tinta = area / 2

print(f'A área de uma parede {altura}x{largura} é de {area} m².')
print(f'A quantidade de tinta que vai precisar para pintar será de {tinta} L.')