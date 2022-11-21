def fatorial(number, show=False):
    """
    -> Calcula o fatorial de um número.
    :param number: O número a ser calculado.
    :param show: Valor que controla se será exibido ou não o calculo.
    :return: o valor do fatorial de um número.
    """

    f = 1
    for c in range(number, 0, -1):
        if show:
            print(f'{c} ', end='')
            if c > 1:
                print('x ', end='')
            else:
                print('= ', end='')
        f *= c
    print(f)


print('-'*30)
#fatorial(5, False)
help(fatorial)
