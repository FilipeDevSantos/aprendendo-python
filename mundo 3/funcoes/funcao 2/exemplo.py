
# função com retorno e parâmetros opcionais
def aoQuadrado(a=0):
    """
    ----> Faz uma conta de exponienciação e retorna o resultado.
    :param a: número a ser elevado (opcional).
    :return: um valor númerico.
    """

    # fazendo conta usando variável global e local
    result = a ** quadrado

    return result


# VARIÁVEL GLOBAL
quadrado = 2
numero = 3

help(aoQuadrado)
print('-'*30)
print(f'O resultado do número {numero} ao quadrado é {aoQuadrado(numero)}')
