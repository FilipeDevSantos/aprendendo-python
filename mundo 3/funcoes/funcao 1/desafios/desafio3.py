from time import sleep


def contagem(inicio, fim, passo=1):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print('-='*30)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}.')
    if inicio >= fim:
        count = inicio
        while count >= fim:
            print(f' {count}', end='', flush=True)
            sleep(0.2)
            count -= passo
    else:
        count = inicio
        while count <= fim:
            print(f' {count}', end='', flush=True)
            sleep(0.2)
            count += passo
    print(' FIM')

contagem(1, 10, 1)
contagem(10, 0, 2)
print('-='*30)
print('Agora é a sua vez de personalizar a contagem!')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contagem(inicio, fim, passo)