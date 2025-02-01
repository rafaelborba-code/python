def notas(*notas, situation = False):
    dic = {}
    lista = notas
    dic['Total'] = len(lista)
    dic['Maior'] = max(lista)
    dic['Menor'] = min(lista)
    dic['Média'] = sum(lista) / dic['Total']

    if situation == True:
        if 0 <= dic['Média'] < 5:
            dic['Situação'] = 'RUIM'
        if 5 <= dic['Média'] <= 7:
            dic['Situação'] = 'RAZOÁVEL'
        else:
            dic['Situação'] = 'ÓTIMA'

    return dic
result = notas(7.0, 8.0, 8.0, situation=True)
for k, v in result.items():
    print(f'{k} = {v}')