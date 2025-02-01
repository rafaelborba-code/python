import urllib.request

try:
    site = urllib.request.urlopen('https://www.youtube.com/')
except Exception as erro:
    print('Erro ao acessar o site.')
    print(erro)
else:
    print('Site acessado com sucesso!')
    print(site.read())