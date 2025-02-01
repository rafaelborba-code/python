def format(number):
    new = f'R${number:.2f}'.replace(".", ",")
    return new

def metade(number, format_option = True):
    half = number / 2
    if format_option == True:
        return format(half)
    else:
        return half

def dobro(number, format_option = True):
    times2 = number * 2
    if format_option == True:
        return format(times2)
    else:
        return times2

def aumentar(number, taxa, format_option = True):
    aumentar_porcentagem = number * (1 + taxa/100)
    if format_option == True:
        return format(aumentar_porcentagem)
    else:
        return aumentar_porcentagem

def diminuir(number, taxa, format_opinion = True):
    diminuir_porcentagem = number * (1 - (taxa/100))
    if format_opinion == True:
        return format(diminuir_porcentagem)
    else:
        return diminuir_porcentagem
    
def resumir(number, taxa_mais, taxa_menos):
    dic = {
        'Preço analisado':format(number),
        'Dobro do preço':dobro(number),
        'Metade do preço':metade(number),
        f'{taxa_mais}% de aumento':aumentar(number, taxa_mais),
        f'{taxa_menos}% de redução':diminuir(number, taxa_menos)
        }
    return dic