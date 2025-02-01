import money

def titulo(texto):
    print('-'*(len(texto)+12))
    print(f'{texto:^{len(texto)+12}}')
    print('-'*(len(texto)+12))

preco = float(input('Digite o preço: R$'))
taxa_mais = int(input('Taxa de aumento: '))
taxa_menos = int(input('Taxa de redução: '))

titulo('RESUMO DO VALOR')
for k, v in money.resumir(preco, taxa_mais, taxa_menos).items():
    print(f'{k}: {v}')
print('-'*27)