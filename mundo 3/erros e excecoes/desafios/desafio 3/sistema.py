def info():
    print('-' * 30)
    print('{:^30}'.format('SISTEMA MODULARIZADO'))
    print('-' * 30)
    print('Informe o que deseja fazer:')
    print('(1) - Cadastrar uma nova pessoa')
    print('(2) - Listar pessoas cadastradas')
    print('(3) - Exibir o menu novamente')
    print('(0) - Sair do programa')


def newPerson():
    print('-'*30, ' Nova Pessoa ', '-'*30)
    name = str(input('Digite o nome da pessoa: '))

    while True:
        try:
            age = int(input('Digite a idade: '))

            file = open('people.txt', 'a')
            file.write(f'{name}, {age}\n')
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite uma opção válido!\033[m')
        else:
            print('\033[32mCadastrado com sucesso!\033[m')
            break


def listOfPeople():
    people = list()
    person = dict()

    # pegando o arquivo com as informações
    file = open('people.txt', 'r')

    # pegando os dados de cada linha do arquivo de forma separada para poder ter um maior controle na exibição
    for p in file.readlines():
        per = p.split(', ')
        person['name'] = per[0]
        person['age'] = per[1]
        people.append(person.copy())
        person.clear()

    # exibindo os dados
    print('-' * 15, ' Lista de Pessoas ', '-' * 15)
    for c in range(0, len(people)):
        print(f'{c + 1}º Pessoa:\n\tnome: {people[c]["name"]}\n\tidade: {people[c]["age"]}')


def start():
    info()
    while True:
        try:
            option = int(input('Opção: '))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite uma opção válido!\033[m')
            print('-'*30)
        except KeyboardInterrupt:
            print('\033[31mPercebemos que você optiou por não continuar com o programa!\033[m')
            break
        else:
            if option == 0:
                break
            elif option == 3:
                info()
            elif option == 1:
                newPerson()
            elif option == 2:
                listOfPeople()
    print('\033[33mPrograma finalizado!\033[m')
