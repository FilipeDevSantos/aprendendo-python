from random import choice

aluno1 = str(input('Qual o nome do 1º aluno? '))
aluno2 = str(input('Qual o nome do 2º aluno? '))
aluno3 = str(input('Qual o nome do 3º aluno? '))
aluno4 = str(input('Qual o nome do 4º aluno? '))

sorteado = choice([aluno1, aluno2, aluno3, aluno4])

print(f'O aluno sorteado foi {sorteado}.')