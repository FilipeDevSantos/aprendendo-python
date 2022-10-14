while True:
    print('='*50)
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('='*50)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{c} x {n} = {c*n}')
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')