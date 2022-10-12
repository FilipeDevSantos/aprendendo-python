lado1 = int(input('Digite o tamanho do 1º lado: '))
lado2 = int(input('Digite o tamanho do 2º lado: '))
lado3 = int(input('Digite o tamanho do 3º lado: '))

if lado3 > lado1 + lado2 or lado1 > lado2 + lado3 or lado2 > lado1 + lado3:
    print('Não podem formar um triângulo!')
else:
    print('Pode formar triângulos que podem ser ', end='')
    if lado1 == lado2 and lado1 == lado3:
        print('equiláteros.')
    elif lado1 == lado2 or lado2 == lado3:
        print('isósceles.')
    else:
        print('escalenos.')