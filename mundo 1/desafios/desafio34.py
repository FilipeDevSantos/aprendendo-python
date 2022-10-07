salario = float(input('Qual o seu salário? '))
if salario > 1250:
    novo_salario = salario + ((salario * 10) / 100)
    print(f'O seu salário passou a ser {novo_salario} com o novo aumento.')
else:
    novo_salario = salario + ((salario * 15) / 100)
    print(f'O seu salário passou a ser {novo_salario} com o novo aumento.')