import ex109.money as money

preco = float(input('Digite o preço: R$'))
metade = money.half(preco)
x2 = money.times2(preco)
dez_porcento = money.raise_tenpercent(preco)
print(f'O metade de {money.format(preco)} é {money.format(metade)}')
print(f'O dobro de {money.format(preco)} é {money.format(x2)}')
print(f'Aumentando {money.format(preco)} em 10%, temos {money.format(dez_porcento)}')