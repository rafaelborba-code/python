lista = []
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    continuar = input('Quer continuar? [S/N] ').lower()
    if continuar != 's':
        break
print('=-'*25)
print(f'Você digitou {len(lista)} elementos')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são: {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista! ')
else: 
    print('O valor 5 não faz parte da lista!')