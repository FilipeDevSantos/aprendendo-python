pessoas = list()
pessoa = list()
mai = men = 0

while True:
    pessoa.append(str(input('Nome: ')))
    pessoa.append(float(input('Peso: ')))

    if len(pessoas) == 0:
        mai = men = pessoa[1]
    else:
        if pessoa[1] > mai:
            mai = pessoa[1]
        elif pessoa[1] < men:
            men = pessoa[1]
    pessoas.append(pessoa[:])
    pessoa.clear()

    continuar = str(input('Quer continuar? [S/N] ').lower())
    if continuar == 'n':
        break

print('-='*50)
print(f'Você cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso foi {mai}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == mai:
        print(f' {p[0]}', end='')
print(f'\nO menor peso foi {men}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == men:
        print(f' {p[0]}', end='')