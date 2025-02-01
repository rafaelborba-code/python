def maior(* valores):
    lista = valores
    maior = 0
    print('Analisando os valores passados...')
    for i, valor in enumerate(lista):
        print(valor, end=' ')
        if i == 0:
            maior = valor
        if valor > maior:
            maior = valor
    print(f'\nForam informados {len(lista)} valores ao todo.')
    print(f'O maior valor informado foi {maior}')

def linha():
    print('-='*25)


linha()
maior(2, 9, 4, 5, 7, 1)
linha()
maior(4, 7, 0)
linha()
maior(1, 2)
linha()
maior(6)
linha()
maior()
linha()