try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except ZeroDivisionError:
    print('Não é possível fazer divisões onde o zero é o denominador!')
except (ValueError, TypeError):
    print('Tivemos um problema com o tipo de dado informado!')
except KeyboardInterrupt:
    print('Vimos que você preferiu não informar os dados!')
else:
    print(f'O valor da divisão foi {r}.')
finally:
    print('Obrigado pela interação!\nVolte sempre :)')