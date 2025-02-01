import os
import shutil

diretorio = "C:/Users/MoBill Adm/Documents/estudos/python/projeto-organizacao-arquivos/arquivos"

arquivos = os.listdir(diretorio)

# Passo 1: Identificar os tipos de arquivo em uma pasta
# Passo 2 : Criar subpastas para cada tipo de arquivo
#   Se a subpasta já existir, não duplicar pastas e adicionar à pasta existente

# Passo 3: Mover os arquivos para sua respectiva subpasta
if "foto1.jpg" in arquivos:
    os.makedirs("C:/Users/MoBill Adm/Documents/estudos/python/projeto-organizacao-arquivos/arquivos/jpg", exist_ok = True)

    shutil.move("C:/Users/MoBill Adm/Documents/estudos/python/projeto-organizacao-arquivos/arquivos/foto1.jpg", "C:/Users/MoBill Adm/Documents/estudos/python/projeto-organizacao-arquivos/arquivos/jpg/foto1.jpg")

if "doc1.pdf" in arquivos:
    os.makedirs("C:/Users/MoBill Adm/Documents/estudos/python/projeto-organizacao-arquivos/arquivos/pdf", exist_ok = True)

    shutil.move("C:/Users/MoBill Adm/Documents/estudos/python/projeto-organizacao-arquivos/arquivos/doc1.pdf", "C:/Users/MoBill Adm/Documents/estudos/python/projeto-organizacao-arquivos/arquivos/pdf/doc1.pdf")

if "foto2.png" in arquivos:
    os.makedirs("C:/Users/MoBill Adm/Documents/estudos/python/projeto-organizacao-arquivos/arquivos/png", exist_ok = True)

    shutil.move("C:/Users/MoBill Adm/Documents/estudos/python/projeto-organizacao-arquivos/arquivos/foto2.png", "C:/Users/MoBill Adm/Documents/estudos/python/projeto-organizacao-arquivos/arquivos/png/foto2.png")

if "notas.txt" in arquivos:
    os.makedirs("C:/Users/MoBill Adm/Documents/estudos/python/projeto-organizacao-arquivos/arquivos/txt", exist_ok = True)

    shutil.move("C:/Users/MoBill Adm/Documents/estudos/python/projeto-organizacao-arquivos/arquivos/notas.txt", "C:/Users/MoBill Adm/Documents/estudos/python/projeto-organizacao-arquivos/arquivos/txt/notas.txt")