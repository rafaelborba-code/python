from random import randint

print('-'*40)
print('{:^40}'.format('JOGANDO NA MEGA SENA'))
print('-'*40)

jogos = int(input('Quantos jogos você quer que eu sorteie? '))
print('-='*3,f'SORTEANDO {jogos} JOGOS ', '=-'*3)

jogo = []

for c1 in range(0,jogos):
    while len(jogo) < 6:
        n = randint(1,60)
        if not n in jogo:
            jogo.append(n)
    print(f'Jogo {c1+1}: {jogo}')
    jogo.clear()
print('-='*5, '< BOA SORTE! >','=-'*5)