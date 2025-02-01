import pyautogui
from time import sleep

# Passo 1: Abrir o sistema da empresa.
#     Sistema: https://dlp.hashtagtreinamentos.com/python/intensivao/login

pyautogui.PAUSE = 1

pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press("enter")

# Passo 2: Fazer Login

sleep(1.5)

pyautogui.press('tab')
pyautogui.write('email@email.com')
pyautogui.press('tab')
pyautogui.write('123123123')
pyautogui.press('enter')

# Passo 3: Importar a base de dados dos produtos

import pandas as pd
tabela = pd.read_csv("C:/Users/MoBill Adm/Documents/estudos/python/jornadapython/1-automacao/produtos.csv")
print(tabela)

# Passo 4: cadastrar um produto até acabar os produtos

sleep(1)
for linha in tabela.index:
    pyautogui.click(x=715, y=290)
    codigo = tabela.loc[linha, 'codigo']
    pyautogui.write(codigo)
    pyautogui.press('tab')
    marca = tabela.loc[linha, 'marca']
    pyautogui.write(marca)
    pyautogui.press('tab')
    tipo = tabela.loc[linha, 'tipo']
    pyautogui.write(tipo)
    pyautogui.press('tab')
    categoria = tabela.loc[linha, 'categoria']
    pyautogui.write(str(categoria))
    pyautogui.press('tab')
    preco_unitario = tabela.loc[linha, 'preco_unitario']
    pyautogui.write(str(preco_unitario))
    pyautogui.press('tab')
    custo = tabela.loc[linha, 'custo']
    pyautogui.write(str(custo))
    pyautogui.press('tab')
    obs = str(tabela.loc[linha, 'obs'])
    if obs != 'nan':
        pyautogui.write(obs)        
        
    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.scroll(10000)


codigo,marca,tipo,categoria,preco_unitario,custo,obs

# pyautogui.click -> clicar
# pyautogui.press -> pressionar uma tecla do teclado
# pyautogui.write -> escrever
# pyautogui.hotkey -> atalho