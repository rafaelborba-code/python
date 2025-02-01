# Fazer um menu para cadastro de pessoas
#   115a: Criar a interface do menu
#       Passo 1: Criar uma função para os títulos(uma para linhas e outra para centralizar)
#       Passo 2: Escrever as informações com cores

from lib.interface import *
from lib.arquivo import *

arquivo = 'cadastrados.txt'

if not ArquivoExiste(arquivo):
    criarArquivo(arquivo)

menu(arquivo)