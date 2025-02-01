valores = []
continuar = ''
while True:
    n = int(input('Digite um valor: '))
    if valores.count(n)>=1:
        print('Valor duplicado! Não vou adicionar...')
    elif valores.count(n) <= 1:
        print('Valor adicionado com sucesso...')
        valores.append(n)
    continuar = input('Quer continuar? [S/N] ').strip().lower()
    if continuar != 's':
        break
print('=-'*25)
valores.sort()
print(f'Você digitou os valores {valores}')
