def titulo(titulo):
    print('-'*40)
    print(f'{titulo:^40}')
    print('-'*40)

def area(l, c):
    area = l*c
    print(f'A área de um terreno {l}x{c} é {area}m²')


titulo('Controle de Terrenos')
largura = float(input('LARGURA (m):'))
comprimento = float(input('COMPRIMENTO (m):'))
area(largura, comprimento)