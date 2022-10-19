from time import sleep


def maior(* num):
    print('-='*30)
    print('Analisando os valores passados...')
    num_maior = 0
    for c in range(0, len(num)):
        print(f'{num[c]} ', end='', flush=True)
        sleep(0.5)
        if num[c] > num_maior:
            num_maior = num[c]
    print(f'foram informado {len(num)} valores ao todo')
    print(f'O maior número é {num_maior}.')

maior(2, 3, 4, 3412, 21, 3)
maior(2, 5, 8, 23)
maior(0, 1, 0, -1)