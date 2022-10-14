print('='*50)
print('{:^50}'.format('BANCO JDV'))
print('='*50)

valor = float(input('Qual valor você deseja sacar? R$'))

acima_cem = 0
print('\nTOTAL DE:')
while True:
    cinquenta = int(valor/50)
    valor = valor % 50
    if cinquenta > 0:
        print(f' * {cinquenta} cédulas de $50')
        if valor == 0:
            break
    vinte = int(valor/20)
    valor = valor % 20
    if vinte > 0:
        print(f' * {vinte} cédulas de R$20')
        if valor == 0:
            break
    dez = int(valor/10)
    valor = valor % 10
    if dez > 0:
        print(f' * {dez} cédulas de R$10')
        if valor == 0:
            break
    um = int(valor/1)
    valor = valor % 1
    if um > 0:
        print(f' * {um} cédulas de R$1')
    break
print('='*50)
print('Volte sempre ao BANCO JDV! Tenha um bom dia!\n')