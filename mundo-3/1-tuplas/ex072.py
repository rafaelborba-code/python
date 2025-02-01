nums = (
    "zero", "um", "dois", "três", "quatro", "cinco", 
    "seis", "sete", "oito", "nove", "dez", "onze", 
    "doze", "treze", "catorze", "quinze", "dezesseis", 
    "dezessete", "dezoito", "dezenove", "vinte"
)
while True:
    n = int(input('Digite um número entre 0 e 20: '))
    if n >= 0 and n <= 20:
        extenso = nums[n]
        print(f'Você digitou o número {extenso}')
        break
    else:
        print('Tente novamente.',end=' ')