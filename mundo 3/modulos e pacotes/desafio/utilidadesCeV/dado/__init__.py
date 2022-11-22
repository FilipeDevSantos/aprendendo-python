def leiaDinheiro(msg):
    while True:
        num = str(input(msg)).replace(',', '.').strip()

        if num.isalnum() or num == '':
            print(f'\033[31mERRO: "{num}" é um preço inválido!\033[m')
        else:
            return float(num)
