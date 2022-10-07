cidade = str(input('Qual é a sua cidade? '))

tem_santos = "SANTOS" in cidade.split()[0].upper()

print(f'Sua cidade têm SANTOS no começo? {tem_santos}')