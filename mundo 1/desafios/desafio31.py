distancia = float(input('Qual a distância da viagem em km? '))
if distancia <= 200:
    passagem = distancia * 0.5
    print(f'Como não é uma viagem tão longa, você vai ter que pagar R$ {passagem}.')
else:
    passagem = distancia * 0.45
    print(f'Olha, essa viagem é um pouco longa e por isso você vai apenas pagar R$ {passagem}.')