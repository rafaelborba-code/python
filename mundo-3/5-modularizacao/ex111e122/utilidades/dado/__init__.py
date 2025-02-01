def lerDinheiro(perg):
    while True:
        preco = input(perg).replace(',','.', 1).strip()
        if preco.isalpha():
            print(f'\033[1;31mERRO! O preço \'{preco}\' não é válido.\033[m')
        else:
            break
    return float(preco)