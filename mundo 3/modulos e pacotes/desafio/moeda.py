def dobro(num):
    return num * 2


def metade(num):
    return num / 2


def aumentar(num, quant):
    return num + (num * quant) / 100


def diminuir(num, quant):
    return num - (num * quant) / 100


def moeda(num):
    text = "R${preco:.2f}"
    result = text.format(preco=num)
    return result.replace('.', ',')
