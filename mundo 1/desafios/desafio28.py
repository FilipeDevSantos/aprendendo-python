from random import randint

numero_maquina = randint(0, 5)
print('Pensei em um número!')
numero_escolhido = int(input('Tente adivinhar humano: '))
if numero_escolhido == numero_maquina:
    print('é parece que humano não são tão ruins!')
else:
    print('As máquinas sempre serão superiores!')