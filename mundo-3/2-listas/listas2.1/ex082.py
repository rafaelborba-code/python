lista = []
impar = []
par = []
while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    continuar = input('Quer continuar? [S/N] ').lower()
    if n % 2 == 0:
        par.append(n)
    elif n % 2 != 0:
        impar.append(n)
    if continuar != 's':
        break
print('=-'*25)
print(f'A lista de números completa é: {lista}')
print(f'A lista de números ímpares é: {impar}')
print(f'A lista de números pares é: {par}')