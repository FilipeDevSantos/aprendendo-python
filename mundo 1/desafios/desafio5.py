algo = input('Digite algo: ')

print('o tipo primitivo de {} é: {}.'.format(algo, type(algo)))
print('{} é alfanúmerico? {}.'.format(algo, algo.isalnum()))
print('{} é alfabetico? {}.'.format(algo, algo.isalpha()))
print('{} é um espaço? {}.'.format(algo, algo.isspace()))
print('{} está em maiúsculo? {}.'.format(algo, algo.isupper()))
print('{} está em minúsculo? {}.'.format(algo, algo.islower()))
print('{} é númerico? {}.'.format(algo, algo.isnumeric()))
print('{} está capitalizado? {}.'.format(algo, algo.istitle()))
