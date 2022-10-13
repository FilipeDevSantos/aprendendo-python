pessoas_maiores = 0
pessoas_menores = 0
for c in range(0, 7):
    ano = int(input('Informe o ano de nascimento: '))
    idade = 2022 - ano
    if idade > 18:
        pessoas_maiores += 1
    else:
        pessoas_menores += 1
print(f'Nesse grupo de pessoas, {pessoas_maiores} são de maior e {pessoas_menores} são de menor')