tupla = (
    'Lápiz',
    1.75,
    'Borracha',
    2.0,
    'Caerno',
    15.9,
    'Estojo',
    25.0,
    'Transferidor',
    4.2,
    'Conpasso',
    9.99,
    'Mochila',
    120.32,
    'Canetas',
    22.3,
    'Livro',
    34.9
)

print('-'*50)
print('{:^50}'.format('LISTAGEM DE PREÇOS'))
print('-'*50)

for c in range(0, len(tupla), 2):
    prox = c + 1
    print('{:.<42}R$ {:.2f}'.format(tupla[c], tupla[prox]))
print('-'*50)