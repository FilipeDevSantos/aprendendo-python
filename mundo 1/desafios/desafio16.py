dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))

preco_aluguel = (dias * 60) + (km * 0.15)

print(f'O valor a se pagar será de R${preco_aluguel:.2f}.')