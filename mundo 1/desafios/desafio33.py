numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite um segundo número: '))
numero3 = int(input('Digite um terceiro número: (juro que esse é o ultimo) '))

if numero1 > numero2 and numero1 > numero3:
    print(f'O maior número é o {numero1}.')
    print(f'E o menor número é o {numero2 if numero2 < numero3 else numero3}.')
elif numero2 > numero3:
    print(f'O maior número é o {numero2}.')
    print(f'E o menor número é o {numero1 if numero1 < numero3 else numero3}.')
else:
    print(f'O maior número é o {numero3}.')
    print(f'E o menor número é o {numero1 if numero1 < numero2 else numero2}.')