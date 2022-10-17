aluno = dict()
nome = str(input('Nome: '))
media = float(input(f'Média de {nome}: '))
if media >= 7:
    aluno['situacao'] = 'Aprovado'
else:
    aluno['situacao'] = 'Reprovado'
print(f'Nome é igual a {nome}.')
print(f'Média é igual a {media}.')
print('Situação é igual a {}.'.format(aluno['situacao']))