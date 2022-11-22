import moeda


preco = int(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(preco)} é {moeda.metade(preco, show=True)}.')
print(f'O dobro de {moeda.moeda(preco)} é {moeda.dobro(preco, show=True)}.')
print(f'Aumentando 10%, temos {moeda.aumentar(preco, 10, show=True)}.')
print(f'Diminuindo 13%, temos {moeda.diminuir(preco, 13, show=True)}.')
