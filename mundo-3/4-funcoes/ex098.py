from time import sleep

def linha():
    print('-='*20)

def contador(inicio, fim, passo):
    if passo == 0:
        print(f'Passo igual a 0 inválido. Convertendo para 1...')
        passo = 1
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if inicio < fim:
        for c in range (inicio, fim+1, passo):
            print(c, end=' ', flush=True)
            sleep(0.5)
    if inicio > fim:
        for c in range (inicio, fim-1, passo*-1):
            print(c, end=' ', flush=True)
            sleep(0.5)
    print('FIM!')
linha()
contador(1, 10, 1)
linha()
contador(10,0, 2)
linha()
print('Agora é a sua vez de personalizar a contagem!')
i = int(input(f"{'Início: ':<8}"))
f = int(input(f"{'Fim: ':<8}"))
p = int(input(f"{'Passo: ':<8}"))
contador(i, f, p)