def leiaInt(msg):
    while True:
        try:
            num = str(input(msg))
            response = int(num)
        except ValueError:
            print('\033[31mERRO: por favor, Digite um número inteiro válido.\033[m')
        else:
            return response


def leiaFloat(msg):
    while True:
        try:
            num = str(input(msg))
            response = float(num)
        except ValueError:
            print('\033[31mERRO: por favor, Digite um número real válido.\033[m')
        else:
            return response


try:
    inteiro = leiaInt('Digite um número inteiro: ')
    real = leiaFloat('Digite um número real: ')
except KeyboardInterrupt:
    print('\n\033[31mUsuário preferiu não digitar os números.\033[m')
else:
    print(f'O número inteiro que você digitou foi {inteiro} e o real foi {real}.')
finally:
    print('\033[32mPrograma finalizado!\nVolte sempre :)\033[m')