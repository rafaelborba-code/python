import money
preco = float(input('Digite o preço: R$'))
print(f'A metade de R${preco:.2f} é {money.half(preco):.2f}.')
print(f'O dobro de R${preco:.2f} é {money.times2(preco):.2f}.')
print(f'Aumentando R${preco:.2f} em 10%, temos {money.raise_tenpercent(preco):.2f}.')