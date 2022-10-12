from random import choice
from emoji import emojize

print('Vamos jogar?')
print('='*40)
print(' '*16, 'JOKENPÔ', ' '*16)
humano = str(input('\nEscolha pedra papel ou tesoura: '))
if humano == 'pedra' or humano == 'papel' or humano == 'tesoura':
    maquina = choice(['pedra', 'papel', 'tesoura'])
    print(f'Eu joguei {maquina}.')
    if humano == 'pedra' and maquina == 'papel' or humano == 'papel' and maquina == 'tesoura' or humano == 'tesoura' and maquina == 'pedra':
        print('O óbvio continua óbvio, eu ganhei!')
    elif humano == maquina:
        print('Dessa vez empatamos, mas da proxima apenas um irá ganhar!')
    else:
        print(emojize('Parabéns humano :unamused_face: .', language='en'))
else:
    print('Opção inválida!')