# colocar cores
cor = [
    '\033[m', # 0 - sem cor
    '\033[1;42m', # 1 - verde
    '\033[1;44m', # 2 - azul
    '\033[1;41m', # 3 - vermelho
    '\033[30;47m' # 4 - fundo branco, letra preta
]

def title(text, n):
    print(cor[n],end='')
    print('~'*(len(text)+6))
    print(f'{text:^{len(text)+6}}')
    print('~' * (len(text) + 6))
    print(cor[0])


# fazer um sistema de ajuda usando interactive help
from time import sleep

def ajuda(cmd):
    print(cor[4])
    help(cmd) 
    print(cor[0])
    sleep(1)

while True:  
    title('Sistema de Ajuda PyHelp', 1)
    resp = input('Função ou biblioteca > ') # Passo 1: perguntar o comando 
    if resp.lower().strip() != 'fim':
        title(f'Acessando o manual do comando \'{resp}\'...', 2)
        sleep(1)
        ajuda(resp) # Passo 2: mostrar o interactive help do comando (4)
    else: 
        title('ATÉ LOGO!', 3)
        break
#   Passo 3: repetir o processo até o usuário digitar fim
