sexo = ''
pessoa = dict()
pessoas = list()
mulheres = list()
media = 0

while True:
    pessoa['nome'] = str(input('Nome: '))
    while sexo != 'F' and sexo != 'M':
        sexo = str(input('Sexo: [M/F] ').upper())
    pessoa['sexo'] = sexo
    pessoa['idade'] = int(input('Idade: '))
    pessoas.append(pessoa.copy())
    continuar = str(input('Quer continuar? [S/N] ').lower())
    if continuar == 'n':
        break
for c in range(0, len(pessoas)):
    media += pessoas[c]['idade']
    if pessoas[c]['sexo'] == 'F':
        mulheres.append(pessoas[c]['nome'])
media /= len(pessoas)

print('-='*30)
print(f'- O grupo tem {len(pessoas)} pessoas.')
print(f'A média de idade é de {media} anos.')
print('As mulheres cadastradas foram ', end='')
for mulher in mulheres:
    print(f' {mulher}', end='')
print('\n- Lista de pessoas que estão a cima da média:')
print('-'* 32)
print('| {:^5} {:^6} {:^6}'.format('NOME', 'SEXO', 'IDADE'))
for c in range(0, len(pessoas)):
    if pessoas[c]['idade'] > media:
        print('| {:^5} {:^6} {:^6}'.format(pessoas[c]['nome'], pessoas[c]['sexo'], pessoas[c]['idade']))
print('-'* 32)
print('<< ENCERRADO >>')