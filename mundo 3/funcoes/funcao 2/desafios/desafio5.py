def notas(*notas, sit=False):
    """
    -> Elabora uma série de calculos e retorna informações sobre a respeito de um aluno.
    :param notas: aceita uma ou mais notas.
    :param sit: (opicional) Se deseja também ver qual a situação daquele aluno de acordo com a média.
    :return: um dicionaário com todas as informações solicitadas.
    """

    maior = notas[0]
    menor = notas[0]
    quant_notas = 0
    total = 0
    for c in range(len(notas)):
        if notas[c] > maior:
            maior = notas[c]
        if notas[c] < menor:
            menor = notas[c]
        total += notas[c]

    media = total / len(notas)
    if sit:
        situacao = 'boa' if media >= 6 else 'ruim'
        return {'quantidade_notas': len(notas), 'maior_nota': maior, 'menor_nota': menor, 'media': media,
                'situação': situacao}
    else:
        return {'quantidade_notas': len(notas), 'maior_nota': maior, 'menor_nota': menor, 'media': media}


info = notas(6, 6, 8, 4, sit=True)
print(info)
