termo = int(input('Digite o termo: '))
razao = int(input('Digite a razão: '))
c = 1
while c < 11:
    if c != 10:
        print(f'{termo} -> ', end='')
    else:
        print(f'{termo}')
    termo += razao
    c += 1
a_mais = 1
while a_mais != 0:
    c = 1
    a_mais = int(input('\nQuantos termos a mais você quer ver? '))
    while a_mais != 0 and c < a_mais + 1:
        if c != a_mais:
            print(f'{termo} -> ', end='')
            c += 1
        else:
            print(f'{termo}')
            c += 1
        termo += razao
print('ACABOU')