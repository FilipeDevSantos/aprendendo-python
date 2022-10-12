ano_nasceu = int(input('Em que ano você nasceu? '))
idade = 2022 - ano_nasceu

print('Sua categoria é: ', end='')
if idade <= 9:
    print('MIRIM')
elif idade > 9 and idade <= 14:
    print('INFANTIL')
elif idade > 14 and idade <= 19:
    print('JUNIOR')
elif idade > 19 and idade <= 20:
    print('SENIOR')
else:
    print('MASTER')