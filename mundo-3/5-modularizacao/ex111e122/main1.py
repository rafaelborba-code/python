from utilidades import moeda

for k, v in moeda.resumir(100,50,50).items():
    print(f'{k}:{v}')
