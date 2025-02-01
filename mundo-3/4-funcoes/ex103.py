def ficha_jogador(jogador = '<desconhecido>', gols ='0'):
    print(f"O jogador {jogador} fez {gols} gol(s) no campeonato.")


nome = str(input('Nome do Jogador: '))
num = str(input('Número de gols: '))

if num.isnumeric():
    num = int(num)
else: 
    num = 0
if nome.strip() == '':
    nome = '<desconhecido>'

ficha_jogador(nome, num)