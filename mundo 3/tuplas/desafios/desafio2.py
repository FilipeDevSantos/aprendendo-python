colocados = (
    'Flamengo',
    'Palmeiras',
    'Atlético Mineiro',
    'Grêmio',
    'Athletico Paranaense',
    'Santos',
    'São Paulo',
    'Internacional',
    'Fluminense',
    'Corinthians',
    'Fortaleza',
    'Bahia',
    'Ceará',
    'Cruzeiro',
    'América Mineiro',
    'Atlético Goianiense',
    'Chapecoense',
    'Botafogo',
    'Vasco da Gama',
    'Red Bull Bragantino',
)

print('Lista dos 20 primeiros colocados:')
for index, colocado in enumerate(colocados):
    print(f' {index + 1} - {colocado}')

print(f'5 primeiros colocados:')
for colocado in colocados[:4]:
    print(f' * {colocado}')
print(f'5 ultimos colocados:')
for colocado in colocados[-5:]:
    print(f' * {colocado}')
print('Lista dos 20 primeiros colocados em ordem alfabetica:')
for index, colocado in enumerate(sorted(colocados)):
    print(f' {index + 1} - {colocado}')
print('O time chapecoense está na posição {}.'.format(colocados.index('Chapecoense') + 1))