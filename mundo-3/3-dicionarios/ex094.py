'''A) Quantas pessoas foram cadastradas 
B) A média de idade 
C) Uma lista com as mulheres 
D) Uma lista de pessoas com idade acima da média'''

info = {}
lista = []
mulheres = []
total = 0
sexo = continuar = ''
while True:
    info['Nome'] = input('Nome: ')
    while True:
        sexo = input('Sexo: [M/F] ').lower().strip()[0]
        if sexo not in 'mf':
            print('ERRO! Por favor, digite apenas M ou F.')
        else:
            if sexo == 'f':
                mulheres.append(info['Nome'])
            break
    info['Idade'] = int(input('Idade: '))
    total += info['Idade']
    lista.append(info.copy())
    info.clear()
    while True:
        continuar = input('Quer continuar? [S/N] ').lower().strip()[0]
        if continuar not in 'sn':
            print('ERRO! Por favor, digite apenas S ou N.')
        if continuar in 'sn':
            break
    if continuar == 'n':
        break
media = total / len(lista)
print(f'Pessoas cadastradas: {len(lista)}')
print(f'Média de idade: {media}')
print(f'Mulheres: ',end='')
if len(mulheres)>0:
    print(mulheres)
else:
    print('Nenhuma.')
print(f'Pessoas com idade acima da média: ',end='')
for pessoa in lista:
    if pessoa['Idade'] > media:
        print(pessoa['Nome'], end=' ')