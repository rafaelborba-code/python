# Perguntar nome e peso de alguém até o usuário não querer mais continuar//
# Colocá-los numa lista//
# Pegar o tamanho da lista(quantidade de pessoas cadastradas)//
# Ver o maior peso e o menor//
# Fazer uma lista com as pessoas de maior e menor peso

lista = []
pessoa = []
maior = menor = 0

while True:
    pessoa.append(input('Nome: '))
    pessoa.append(float(input('Peso: ')) )

    if len(lista) == 0:
        maior = menor = pessoa[1]
    if pessoa[1] > maior:
        maior = pessoa[1]
    if pessoa[1] < menor:
        menor = pessoa[1]

    lista.append(pessoa[:]) 
    pessoa.clear()

    continuar = input('Quer continuar? [S/N] ').lower().strip()[0]
    if continuar != 's':
        break

print(f'Ao todo, {len(lista)} pessoas foram cadastradas.') 
print(f'O maior peso foi de {maior} e as pessoas que têm esse peso são:',end=' ')
for pessoa in lista:
    if pessoa[1] == maior:
        print(f'[{pessoa[0]}]', end=' ')
print(f'\nO menor peso foi de {menor} e as pessoas que têm esse peso são:',end=' ')
for pessoa in lista:
    if pessoa[1] == menor:
        print(f'[{pessoa[0]}]',end=' ')
