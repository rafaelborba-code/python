valores = []
maior = menor = 0
for c in range(0,5):
    valores.append(int(input(f'Digite um número para a posição {c}: ')))
    if c == 0:
        maior = menor = valores[c]
    else: 
        if valores[c] > maior:
            maior = valores[c]
        if valores[c] < menor:
            menor = valores[c]
print('=-'*50)
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {maior} nas posições',end=' ')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}...',end='')
print(f'\nO menor valor digitado foi {menor} nas posições',end=' ')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}...',end='')