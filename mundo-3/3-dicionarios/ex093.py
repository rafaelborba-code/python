jogador = {}
gols = []
total = 0

jogador['Nome'] = input('Nome do Jogador: ') 
jogador['Partidas'] = int(input(f'Quantas partidas {jogador["Nome"]} jogou: '))
for c in range(1, jogador['Partidas']+1):
    gol = int(input(f'Gols na partida {c}: ')) 
    gols.append(gol)
    total += gol
jogador['Gols'] = gols
jogador['Total de gols'] = total

print(f'O jogador {jogador["Nome"]} jogou {jogador["Partidas"]} partidas.')
for i, partida in enumerate(gols):
    print(f'-> Na partida {i+1}, {jogador["Nome"]} fez {gols[i]} gols.')
print(f'Total de gols = {jogador["Total de gols"]}')