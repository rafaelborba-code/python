# Fazer um menu para cadastro de pessoas
#   115a: Criar a interface do menu
#       Passo 1: Criar uma função para os títulos(uma para linhas e outra para centralizar)

from lib.arquivo import *

def linha(len = 42):
    return '-' * len

def titulo(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

# Passo 1: Mostrar as opções disponíveis (colorido)
# Passo 2: Perguntar a opção desejada
# Passo 3: detectar a existência da opção respondida pelo usuário
def menu(nome):
    while True:
        titulo('MENU PRINCIPAL')
        print('''\033[33m1\033[m - \033[34mVer pessoas cadastradas\033[m
\033[33m2\033[m - \033[34mCadastrar nova pessoa\033[m
\033[33m3\033[m - \033[34mSair do programa\033[m''')# Números amarelos, texto azul
        print(linha())
        try:
            opc = int(input('\033[32mSua opção: \033[m')) # Verde
        except ValueError:
            print('\033[31mERRO: Valor inválido, digite um número inteiro de 1 a 3 de acordo com as opções\033[m')
        else:
            if 1 <= opc <= 3:
                if opc == 1:
                    titulo('Ver pessoas cadastradas')
                    lerArquivo(nome)
                if opc == 2:
                    titulo('Cadastrar nova pessoa')
                    name = str(input('Nome: '))
                    idade = leiaInt('Idade: ')
                    cadastrar(nome, name, idade)
                if opc == 3:
                    titulo('Saindo do programa...')
                    break
            else:
                print('\033[31mERRO: Digite uma opção válida.\033[m') # Vermelho
#       Passo 2: Escrever as informações com cores