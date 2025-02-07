def twoSum(nums: list[int], target: int) -> list[int]:
    mapa_numeros = {} # vai guardar os números que não derem certo
    for i, num in enumerate(nums):
        complemento = target - num # conferirá o complemento necessário para o número atual
        if complemento in mapa_numeros: 
            return [mapa_numeros[complemento], i] # se o complemento tiver no mapa de números, ele vai retornar o indice do complemento e o indice do numero atual
        mapa_numeros[num] = i #adiciona o numero e seu indice no mapa para ser conferido depois
    return [] #caso não tenha um resultado, será retornado uma lista vazia

print(twoSum([5,2,19,20], 21))
print(twoSum([100, 1000, 1000000], 1))