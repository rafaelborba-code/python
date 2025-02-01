matriz = [
    [],
    [],
    []
]
for c in range(0,3):
    for c2 in range(0,3):
        n = int(input(f'Digite um valor para a posição [{c}, {c2}]: '))
        matriz[c].append(n)
print(f'''[ {matriz[0][0]} ][ {matriz[0][1]} ][ {matriz[0][2]} ]
[ {matriz[1][0]} ][ {matriz[1][1]} ][ {matriz[1][2]} ]
[ {matriz[2][0]} ][ {matriz[2][1]} ][ {matriz[2][2]} ]''')