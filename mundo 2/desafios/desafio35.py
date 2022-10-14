total = passou_mil = mais_barato = 0.0
nome_barato = ''

print('='*50)
print('{:^50}'.format('LOJA SUPER BARATÃO'))
print('='*50)

while True:
    nome = continuar = ''
    nome = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$'))
    while continuar != 'n' and continuar != 's':
        continuar = str(input('Quer continuar? [S/N] ').lower())
    print('-'*50)
    if preco > 1000:
        passou_mil += 1
    if preco < mais_barato or mais_barato == 0:
        mais_barato = preco
        nome_barato = nome
    total += preco
    if continuar == 'n':
        break
print('============= FIM DO PROGRAMA =============')
print(f'Total da compra foi: R${total:.2f}')
print(f'Temos {int(passou_mil)} custando mais de R$1000.00')
print(f'O produto mais barato foi {nome_barato} que custa R${mais_barato:.2f}')