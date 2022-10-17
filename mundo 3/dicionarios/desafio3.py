from datetime import date

pessoa = dict()
pessoa['nome'] = str(input('Nome: '))
ano = int(input('Ano de Nascimento: '))
pessoa['idade'] = date.today().year - ano
pessoa['ctps'] = int(input('Carteira de Trabalho: (0 caso não tenha) '))

if pessoa['ctps'] != 0:
    pessoa['ano_contratação'] = int(input('Ano de contratação: '))
    pessoa['salario'] = float(input('Salário: '))

print('-='*30)
for k, v in pessoa.items():
    print(f'{k} tem o valor {v}.')