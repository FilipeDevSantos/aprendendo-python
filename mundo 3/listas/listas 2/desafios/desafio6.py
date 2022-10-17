alunos = list()
aluno = list()
notas = list()
medias = list()

while True:
    aluno.append(str(input('Nome: ')))
    for c in range(0, 2):
        notas.append(float(input(f'Nota {c+1}: ')))
    aluno.append(notas[:])
    medias.append((notas[0] + notas[1]) / 2)
    notas.clear()
    alunos.append(aluno[:])
    aluno.clear()
    continuar = str(input('Deseja continuar? [S/N] '))
    if continuar == 'n':
        break
print('-='*30)
print('{:<4} {:<13} {}'.format('No.', 'NOME', 'MÉDIA'))
print('-'*30)
for i, a in enumerate(alunos):
    print('{:<4} {:<13} {:>5}'.format(i+1, a[0], medias[i]))
while True:
    print('-'*30)
    desejo = int(input('Mostrar notas de qual aluno? (999 interrompe) '))
    if desejo == 999:
        break
    aluno_desejado = alunos[desejo-1]
    print(f'Notas de {aluno_desejado[0]} são {aluno_desejado[1]}')
print('FINALIZANDO...')
print('<<< VOLTE SEMPRE >>>')