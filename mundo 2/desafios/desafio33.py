from random import randint


vitorias = 0
resultado = ''

while True:
    print('=-'*50)
    print('VAMOS JOGAR PAR OU ÍMPAR')
    print('=-'*50)
    numero = int(input('Digite um valor: '))
    escolha = str(input('Par ou Ímpar? [P/I] ').upper())
    maquina = randint(0, 10)
    total = numero + maquina
    print('-'*50)
    print(f'Você jogou {numero} e a computador {maquina}. Total de {total} ', end='')
    if total % 2 == 0:
        print('DEU PAR')
        print('-'*50)
        resultado = 'P'
    else:
        print('DEU ÍMPAR')
        print('-'*50)
        resultado = 'N'
    if escolha == resultado:
        print('Você venceu!')
        print('Vamos jogar novamente...')
        vitorias += 1
    else:
        print('Você Perdeu!')
        break
print('=-'*50)
print(f'GAME OVER! Você venceu {vitorias} vezes.')