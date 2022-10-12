valor_casa = float(input('Quanto vale a casa? '))
salario = float(input('Qual o valor do seu salário? '))
anos_pagando = int(input('Em quantos anos você pretende pagar? '))

meses_pagando = anos_pagando * 12
mensalidade = valor_casa / meses_pagando
limite_salario = (salario * 30) / 100
consegue_pagar = limite_salario >= mensalidade

print(f'Para pagar uma casa de R${valor_casa} em {anos_pagando} anos', end='')
print(f' a prestação será de R${mensalidade:.2f}.')
if consegue_pagar:
    print('Empréstimo Aprovado!')
else:
    print('Empréstimo Negado!')