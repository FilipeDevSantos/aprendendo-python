def dobro(num, show=False):
    if show:
        return moeda(num * 2)
    else:
        return num * 2


def metade(num, show=False):
    if show:
        return moeda(num / 2)
    else:
        return num / 2


def aumentar(num, quant, show=False):
    if show:
        return moeda(num + (num * quant) / 100)
    else:
        return num + (num * quant) / 100


def diminuir(num, quant, show=False):
    if show:
        return moeda(num - (num * quant) / 100)
    else:
        return num - (num * quant) / 100


def moeda(num):
    text = "R${preco:.2f}"
    result = text.format(preco=num)
    return result.replace('.', ',')


def resumo(preco, aum, dim):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analisado: \t{moeda(preco)}.')
    print(f'Dobro do preço: \t{dobro(preco, show=True)}.')
    print(f'Metade do preço: \t{metade(preco, show=True)}.')
    print(f'80% de aumento: \t{aumentar(preco, aum, show=True)}.')
    print(f'35% de redução: \t{diminuir(preco, dim, show=True)}.')