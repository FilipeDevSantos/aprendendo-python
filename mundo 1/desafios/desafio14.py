salario = float(input('Qual o salário do funcionário? R$ '))

novo_salario = salario + ((salario * 15) / 100)

print(f'O funcionário que ganhava R$ {salario:.2f} com 15% de aumento receberá agora R$ {novo_salario:.2f}.')