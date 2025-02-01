jogador = {}
lista = []
gols = []
total = 0

while True:
# perguntar nome e partidas que um jogador jogou
    jogador['nome'] = input('Nome do jogador: ')
    jogador['partidas'] = int(input(f'Quantidade de partidas jogadas por {jogador['nome']}: '))

# perguntar quantos gols ele fez em cada partida
    for c in range(1, jogador['partidas']+1):
        gol = int(input(f'Gols na partida {c}: '))
        gols.append(gol)
        total += gol

# adicionar tudo em um dicionário e depois numa lista
    jogador['gols'] = gols[:]
    jogador['total de gols'] = total
    lista.append(jogador.copy())
    gols.clear()
    jogador.clear()

    total = 0

# perguntar se o usuário quer continuar
    continuar = input('Quer continuar? [S/N] ').lower().strip()
    if continuar == 'n':
        break
    print('-' * 60)

# mostrar número de cadastro, nome, gols em cada partida e total de gols 
print('-=' * 30)
print(f'N.   Nome           Gols                     Total de gols')
print('-' * 60)
for i, jogador in enumerate(lista):
    print(f'{i:<5}{jogador["nome"]:<15}{str(jogador["gols"]):<30}{jogador["total de gols"]:<15}')

while True:
    print('-' * 60)
# perguntar de qual jogador mostrar os dados
    dados = int(input('Mostrar dados de qual jogador (Responder com o número, 999 para parar): '))
    print('-' * 60)
# mostrar a quantidade de gols em cada jogo do jogador escolhido
    if dados != 999:
        jogador_escolhido = lista[dados]
        print(f'{f'== Levantamento de dados de {jogador_escolhido["nome"]} =='}')
        for i, gols in enumerate(jogador_escolhido['gols']):
            print(f'{jogador_escolhido["nome"]} marcou {jogador_escolhido["gols"][i]} no {i+1}º jogo.')
    else:
        break
print('Encerrado.')