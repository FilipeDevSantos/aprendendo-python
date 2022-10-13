from random import randint

vezes = escolha = 0
maquina = randint(1, 10)
while escolha != maquina:
    escolha = int(input('Escolha um número: '))
    if escolha != maquina:
        print('Você errou!')
        vezes += 1
if vezes > 0:
    print(f'Você acertou, mas para isso você precisou de {vezes} chances.')
else:
    print('Você acertou de primeira!')