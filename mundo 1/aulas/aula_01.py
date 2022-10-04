# Entendendo o funcionamento básico de comandos no python

# quando contém aspas a função print considera que você quer imprimir algo na tela, já que mensagens em python têm essa funcionalidade primordialmente
print('Olá, mundo!')

# quando contém números a função print considera que você quer imprimir algo na tela em caso de número único e caso mais de um, ele considera que será feito calculos matemáticos
print(7+4)

# quando duas mensagens estão separadas pelo +, significa que estamos juntando elas
print('7' + '4')

# variáveis em Python

nome = 'Filipe'
idade = 20
peso = 72.0

print(nome, idade, peso)

# usando inputs para receber valores

nome = input('Qual o seu nome? ')
idade = input('E a sua idade? ')
peso = input('E o seu peso? ')

print(nome, idade, peso)