times = (
    'Botafogo', 'Palmeiras', 'Flamengo', 'Fortaleza', 'Internacional', 
    'São Paulo', 'Corinthians', 'Bahia', 'Cruzeiro', 'Vasco da Gama', 
    'Vitória', 'Atlético-MG', 'Fluminense', 'Grêmio', 'Juventude', 
    'Bragantino', 'Athletico-PR', 'Criciúma', 'Atlético-GO', 'Cuiabá'
)
print(50*'=')
print(f'Lista de times do Brasileirão: \n{times}')
print(50*'=')
print(f'Os 5 Primeiros são: \n{times[:5]}')
print(50*'=')
print(f'Os 4 últimos são: \n{times[16:]}')
print(50*'=')
print(f'Times em ordem alfabética: \n{sorted(times)}')
print(50*'=')
print(f'O Flamengo está na {times.index('Flamengo')+1}ª posição.')
print(50*'=')