extenso = (
    'zero',
    'um',
    'dois',
    'três',
    'quatro',
    'cinco',
    'seis',
    'sete',
    'oito',
    'nove',
    'dez',
    'onze',
    'doze',
    'treze',
    'quartoze',
    'quinze',
    'dezesseis',
    'dezessete',
    'dezoito',
    'dezenove',
    'vinte'
)

while True:
    numero = int(input('Digite um número: '))
    if numero >= 0 and numero <= 20:
        print(f'Você digitou o número {extenso[numero]}.')
        continuar = str(input('Quer continuar? [S/N] '))
        if continuar.lower() == 'n':
            break
    else:
        print('Tente novamente. ', end='')