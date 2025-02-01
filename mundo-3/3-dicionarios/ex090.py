nome = input('Nome: ')
media = float(input(f'Média de {nome}: '))
info = {}
info['Nome'] = nome
info['Média'] = media
if 7 <= media:
    info['Situação'] = 'aprovado'
elif 5 < media < 7:
    info['Situação'] = 'recuperação'
else:
    info['Situação'] = 'reprovado'
print('=-'*10)
for k, v in info.items():
    print(f' - {k} é igual a {v}.')
print()