ano = int(input('Digite o ano em que você nasceu: '))

idade = 2022 - ano

if idade <= 17:
    quanto_falta = 18 - idade
    print(f'Você ainda não pode se alistar, pois falta {quanto_falta} anos para esse dia.')
elif idade == 18:
    print('Você já deve se alistar!')
else:
    anos_a_mais = idade - 18
    print(f'Você já passou do prazo de se alistar, parece que você está atrasado {anos_a_mais} anos.')