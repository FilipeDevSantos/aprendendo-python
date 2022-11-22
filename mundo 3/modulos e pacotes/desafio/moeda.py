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
