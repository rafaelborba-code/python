matriz = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
maior_linha2 = soma_pares = soma_coluna3 = 0
for c in range(0,3):
    for c2 in range(0,3):
        n = int(input(f'Digite um valor para a posição [{c}, {c2}]:'))
        if n % 2 == 0:
            soma_pares += n
        if c == 1:
            if c2 == 0:
                maior_linha2 = n
            if n > maior_linha2:
                maior_linha2 = n
        matriz[c][c2]=n
print('=-'*25)
print(f'''[ {matriz[0][0]} ][ {matriz[0][1]} ][ {matriz[0][2]} ]
[ {matriz[1][0]} ][ {matriz[1][1]} ][ {matriz[1][2]} ]
[ {matriz[2][0]} ][ {matriz[2][1]} ][ {matriz[2][2]} ]''')
print('=-'*25)
print(f'A soma dos valores pares é {soma_pares}')
print(f'A soma dos valores da terceira coluna é {matriz[0][2]+matriz[1][2]+matriz[2][2]}')
print(f'O maior valor da segunda linha é {maior_linha2}')