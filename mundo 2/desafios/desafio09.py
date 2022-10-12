preco = float(input('Digite o preço do produto: R$'))
print('-'*31)
print(' '*2, 'Informe o tipo de pagamento', ' '*2)
print('1 - A vista dinheiro/cheque: 10%. de desconto')
print('2 - A vista no cartão: 5%. de desconto')
print('3 -Em até 2x no cartão: Preço normal')
print('4 - Em 3x ou mais no cartão: 20%. de juros')
opcao = int(input('Opção: '))

if opcao == 1:
    valor_pagar = preco - ((preco * 10) / 100)
    print(f'O valor do produto ficou por R${valor_pagar:.2f}.')
elif opcao == 2:
    valor_pagar = preco - ((preco * 5) / 100)
    print(f'O valor do produto ficou por R${valor_pagar:.2f}.')
elif opcao == 3:
    print(f'O valor do produto ficou por R${preco:.2f}.')
elif opcao == 4:
    valor_pagar = preco + ((preco * 20) / 100)
    print(f'O valor do produto ficou por R${valor_pagar:.2f}.')
else:
    print('Opção inválida!')