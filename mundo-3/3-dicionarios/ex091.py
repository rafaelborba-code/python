from random import randint
from time import sleep
from operator import itemgetter
jogo = {
    'Jogador 1': randint(1,6),
    'Jogador 2': randint(1,6),
    'Jogador 3': randint(1,6),
    'Jogador 4': randint(1,6)
}

print('Valores sorteados: ')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
print('-='*23)

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

print(f'{'== RANKING DOS JOGADORES ==':^46}')
print()
for i, v in enumerate(ranking):
    print(f"{f'{i+1}º lugar: {v[0]} com {v[1]} no dado':^46}")
print()
