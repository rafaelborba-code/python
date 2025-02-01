# Ler nome, nota 1 e 2 e colocar numa lista composta
# Mostrar um boletim com a média, nome e número do aluno
# Perguntar de qual aluno quer mostrar as notas(999 para parar)
aluno = []
lista = []
while True:
    nome = input('Nome: ')
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    aluno.append(nome)
    aluno.append(nota1)
    aluno.append(nota2)
    aluno.append(media)
    lista.append(aluno[:])
    aluno.clear()
    continuar = input('Quer continuar? [S/N] ').lower().strip()[0]
    if continuar == 'n':
        break
print('-='*11)
print(f'No. Nome {'Média':>12}')
print('-'*22)
for c, aluno in enumerate(lista):
    print(f'{c}. {lista[c][0]} {lista[c][3]:>12}')
print('-'*22)

notas_mostrar = 0
while True:
    notas_mostrar = int(input('Mostrar notas de qual aluno? (Responder com o número do aluno, 999 para parar): '))
    if notas_mostrar == 999:
        break
    print(lista[notas_mostrar][1:3])