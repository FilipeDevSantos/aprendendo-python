media_idade = 0
idade_mais_velho = 0
nome_mais_velho = ''
total_mulheres = 0

for c in range(0, 4):
    nome = str(input('Digite seu nome: '))
    idade = int(input('Digite sua idade: '))
    sexo = str(input('''
    Digite seu sexo:
    [ m ] - masculino
    [ f ] - feminino
    sexo: '''))

    media_idade += idade
    if sexo == 'f' and idade > 20:
        total_mulheres += 1
    if sexo == 'm' and idade > idade_mais_velho:
        idade_mais_velho = idade
        nome_mais_velho = nome
print(f'A media de idades das 4 pessoas foi de {media_idade / 4}.')
print(f'O total de mulheres que têm mais de 20 anos é de {total_mulheres}.')
print(f'O nome do homem mais velho é {nome_mais_velho}.')