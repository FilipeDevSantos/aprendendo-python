def header(msg, color=42):
    tam = len(msg)+5
    print(f'\033[1;37;{color}m~'*tam)
    print(f'   {msg}')
    print('~'*tam)
    print('\033[m')


def pyHelp():
    from time import sleep
    while True:
        header('SISTEMA DE AJUDA PyHELP')
        sleep(1)
        command = str(input('Função ou Biblioteca > '))
        if command == 'fim':
            header('ATÉ LOGO!', color=41)
            break
        sleep(1)
        header(f"Acessando o manual do comando '{command}' ", color=44)
        sleep(1)
        print('\033[0;30;47m')
        help(command)
        print('\033[m')
        sleep(1)


pyHelp()
