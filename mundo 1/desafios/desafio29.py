velocidade = float(input('Qual é a sua velocidade? '))
if velocidade > 80:
    print('Você foi multado!')
    multa = (velocidade - 80) * 7
    print(f'O preço da multa a se pagar é de R$ {multa:.2f}.')
else:
    print('Ok, boa viagem!')