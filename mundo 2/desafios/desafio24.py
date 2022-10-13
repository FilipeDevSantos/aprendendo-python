opcao = 0
while opcao != 5:
    numero1 = int(input('Digite o primeiro número: '))
    numero2 = int(input('Digite o segundo número: '))
    opcao = 0

    while opcao != 4 and opcao != 5:
        opcao = int(input('''
Agora escolha o que deseja fazer:
[1] - somar
[2] - multiplicar
[3] - maior
[4] - novos números
[5] - Sair do programa
opcao: '''))

        if opcao == 1:
            print(f'A soma entre {numero1} e {numero2} é igual a {numero1 + numero2}.')
        elif opcao == 2:
            print(f'O número {numero1} vezes o número {numero2} é igual a {numero1 * numero2}.')
        elif opcao == 3:
            print(f'Entre {numero1} e {numero2} o maior número é {numero1 if numero1 > numero2 else numero2}.')
print('Fim do programa.')