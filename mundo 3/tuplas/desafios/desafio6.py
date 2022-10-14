tupla = (
    'APRENDER',
    'PROGRAMAR',
    'PYTHON',
    'DJANGO',
    'DATABASE',
    'DATASIENCE',
    'FLASK',
)

for palavra in tupla:
    print(f'\nNa palavra {palavra} temos ', end='')
    for c in range(0, len(palavra)):
        if palavra[c] == 'A' or palavra[c] == 'E' or palavra[c] == 'I' or palavra[c] == 'O' or palavra[c] == 'U':
            print(f' {palavra[c].lower()}', end='')