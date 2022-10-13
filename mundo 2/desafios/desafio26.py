termo = int(input('Digite o termo: '))
razao = int(input('Digite a razão: '))
c = 0
while c < 10:
    print(f'{termo} -> ', end='')
    termo += razao
    c += 1
print('ACABOU')