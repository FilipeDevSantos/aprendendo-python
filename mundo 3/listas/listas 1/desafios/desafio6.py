e_valido = list()
expressao = str(input('Digite a expressão: '))
for c in expressao:
    if c == '(':
        e_valido.append('(')
    elif c == ')':
        if len(e_valido) > 0:
            e_valido.pop()
        else:
            e_valido.append(')')
if len(e_valido) == 0:
    print('Sua expressão é válida!')
else:
    print('Sua expressão está errada!')