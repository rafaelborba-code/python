def alg_ordenator(num):
    lista=[]
    num = str(num)
    for alg in num:
        alg = int(alg)
        lista.append(alg)
    return sorted(lista)


print(alg_ordenator(84323))