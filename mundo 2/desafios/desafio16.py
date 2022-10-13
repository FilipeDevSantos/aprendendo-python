termo = int(input('Informe o primeiro termo da P.A.: '))
razao = int(input('Agora informe a razão: '))

for c in range(1, 11):
    print(f'{termo} -> ', end='')
    termo += razao
print('ACABOU')