def factorial(n, show=False):
    '''
    -> Calcula o fatorial de um número
    :param1: Número do fatorial calculado
    :param2: Mostra ou não os números multiplicados para chegar no fatorial
    :return: Retorna o fatorial
    '''
    f = 1
    for c in range(n,0,-1):
        f*=c
        if show == True:
            print(f'{c}', end=' ')
    return f


print(factorial(5, show=True))