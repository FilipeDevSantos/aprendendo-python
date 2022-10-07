nome = str(input('Digite seu nome: '))

nome_dividido = nome.split()

print(f'Seu primeiro nome é: {nome_dividido[0]}')
print(f'Seu ultimo nome é: {nome_dividido[len(nome_dividido) - 1]}')