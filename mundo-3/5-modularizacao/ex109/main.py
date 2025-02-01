import money

preco = float(input('Digite o preço: R$'))
metade = money.half(preco, False)
x2 = money.times2(preco)
dez_porcento = money.raise_tenpercent(preco)
print(f'O metade de {money.format(preco)} é {metade}')
print(f'O dobro de {money.format(preco)} é {x2}')
print(f'Aumentando {money.format(preco)} em 10%, temos {dez_porcento}')