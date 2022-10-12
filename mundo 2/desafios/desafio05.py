nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))

media = (nota1 + nota2) / 2
print(f'A sua média foi: {media:.2f}')

if media < 5.0:
    print('REPROVADO!')
elif media >= 5.0 and media < 7:
    print('RECUPERAÇÃO')
else:
    print('APROVADO!')