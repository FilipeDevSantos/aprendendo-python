def leiaInt(msg):
    while True:
        num = str(input(msg))
        if num.isnumeric():
            return num
        else:
            print('\033[31mERRO! Digite um número válido.\033[m')


n = leiaInt('Digite um número: ')
print(f'O número que você digitou foi {n}.')
