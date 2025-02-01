from random import randint
from time import sleep

lista = []
pares = []

def sorteia():
    print('Sorteando 5 valores da lista: ')
    for c in range(0,5):
        lista.append(randint(0, 9))
        print(lista[c], end=' ', flush=True)
        if lista[c] % 2 == 0:
            pares.append(lista[c])
        sleep(0.4)
    print('PRONTO!')

def somaPar():
    somapares = 0
    for v in pares:
        somapares += v
    print(f'Somando os valores pares de {lista}, temos {somapares}')


sorteia()
somaPar()