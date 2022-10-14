mulheres_vinte = homens = maior_idade = 0
while True:
    print('='*50)
    print('CADASTRO DE PESSOAS')
    print('='*50)

    sexo = continuar = ''
    idade = int(input('Idade: '))
    while sexo != 'm' and sexo != 'f':
        sexo = str(input('Sexo: [M/F] ').lower())
    print('-'*50)
    while continuar != 'n' and continuar != 's':
        continuar = str(input('Quer continuar? [S/N] ').lower())
    if idade < 18:
        maior_idade += 1
    if sexo == 'f' and idade < 20:
        mulheres_vinte += 1
    elif sexo == 'm':
        homens += 1
    if continuar == 'n':
        break
print('======== FIM DO PROGRAMA ========')
print(f'Total de pessoas com mais de 18 anos: {maior_idade}')
print(f'Ao todo temos {homens} homens cadastrados')
print(f'E temos {mulheres_vinte} mulher com menos de 20 anos')