def somatorio(* num):
    print(f'Os números recebidos foram {num}.')
    total = 0
    for numero in num:
        total += numero
    print(f'A soma de todos os números deu {total}.')

somatorio(7, 6, 5)