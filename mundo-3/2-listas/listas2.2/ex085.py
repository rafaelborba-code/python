# Ler 7 valores
# Criar uma lista com os ímpares
# Criar uma lista com os pares
numeros = [[],[]]
for c in range(1,8):
    n = int(input(f'Digite o {c}º valor: '))
    if n % 2 == 0:
        numeros[0].append(n)
    else:
        numeros[1].append(n)
print('=-'*25)
print(f'Os valores pares digitados foram: {numeros[0]}')
print(f'Os valores ímpares digitados foram: {numeros[1]}')