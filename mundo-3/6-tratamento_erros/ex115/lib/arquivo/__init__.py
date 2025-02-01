# Criar uma função para saber se o arquivo existe
# Criar uma função para criar o arquivo caso ele não exista

def ArquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    
def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
    except:
        print('Houve um erro na criação do arquivo.')
    else:
        print(f'Arquivo {nome} criado com sucesso.')

def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Houve um erro ao ler o arquivo.')
    else:
        print(a.read())
    finally:
        a.close()

def cadastrar(arq, nome, idade):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um erro na abertura do arquivo.')
    else:
        try:
            a.write(f'{nome:<25}{idade} anos\n')
        except:
            print('Houve um erro ao tentar escrever no arquivo.')
        else:
            print(f'Novo registro de {nome} adicionado')
    finally:
        a.close()

def leiaInt(perg):
    while True:
        try:
            n = int(input(perg))
        except ValueError:
            print(f'\033[1;31mERRO: O valor digitado não é um número inteiro.\033[m')
        else:
            return n