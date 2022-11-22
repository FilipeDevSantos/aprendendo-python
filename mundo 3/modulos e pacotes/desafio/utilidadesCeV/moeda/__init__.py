def dobro(num, show=False):
    """
    -> Faz o calculo para achar o dobro de um número.
    :param num: Número a ser dobrado.
    :param show: (opcional) Se deve ou não formatar.
    :return: O número ao dobro.
    """

    if show:
        return moeda(num * 2)
    else:
        return num * 2


def metade(num, show=False):
    """
    -> Faz o calculo para achar a metade de um número.
    :param num: Número a ficar pela metade.
    :param show: (opcional) Se deve ou não formatar.
    :return: O número pela metade.
    """

    if show:
        return moeda(num / 2)
    else:
        return num / 2


def aumentar(num, quant, show=False):
    """
    -> Aumenta o número em uma porcentagem informada.
    :param num: Número a ser aumentado.
    :param quant: porcentagem usada para aumentar o número.
    :param show: (opcional) Se deve ou não formatar.
    :return: Número aumentado em uma porcentagem informada.
    """

    if show:
        return moeda(num + (num * quant) / 100)
    else:
        return num + (num * quant) / 100


def diminuir(num, quant, show=False):
    """
    -> Diminui o número em uma porcentagem informada.
    :param num: Número a ser diminuido.
    :param quant: porcentagem usada para diminuir o número.
    :param show: (opcional) Se deve ou não formatar.
    :return: Número diminuido em uma porcentagem informada.
    """

    if show:
        return moeda(num - (num * quant) / 100)
    else:
        return num - (num * quant) / 100


def moeda(num):
    """
    -> Deixa o número informado em formato de preço.
    :param num: Número a ser formatado.
    :return: Uma string formatada.
    """

    text = "R${preco:.2f}"
    result = text.format(preco=num)
    return result.replace('.', ',')


def resumo(preco, aum, dim):
    """
    -> Faz uma exibição organizada.
    :param preco: Número base para todas as contas.
    :param aum: Número usado na função de aumentar.
    :param dim: Número usado na função de diminuir.
    :return: Uma string formatada e organizada.
    """

    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analisado: \t{moeda(preco)}.')
    print(f'Dobro do preço: \t{dobro(preco, show=True)}.')
    print(f'Metade do preço: \t{metade(preco, show=True)}.')
    print(f'80% de aumento: \t{aumentar(preco, aum, show=True)}.')
    print(f'35% de redução: \t{diminuir(preco, dim, show=True)}.')
