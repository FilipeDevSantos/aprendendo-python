lado1 = int(input('Digite o tamanho do 1º lado: '))
lado2 = int(input('Digite o tamanho do 2º lado: '))
lado3 = int(input('Digite o tamanho do 3º lado: '))

if lado3 > lado1 + lado2 or lado1 > lado2 + lado3 or lado2 > lado1 + lado3:
    print('podem formar um triângulo!')
else:
    print('Não pode formar um triângulo!')