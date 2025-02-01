from utilidades import dado
from utilidades import moeda

preco = dado.lerDinheiro('Digite um preço: R$')
moeda.resumir(preco, 50, 50)