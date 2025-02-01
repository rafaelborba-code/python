def leiaInt(perg):
    while True:
        try:
            n = int(input(perg))
        except ValueError:
            print(f'\033[1;31mERRO: O valor digitado não é um número inteiro.\033[m')
        else:
            return n

def leiaFloat(perg):
    while True:
        try:
            n = float(input(perg))
        except ValueError:
            print(f'\033[1;31mERRO: O valor digitado não é um número real.\033[m')
        else: 
            return n 


inteiro = leiaInt('Digite um inteiro: ')
real = leiaFloat('Digite um número real: ')
print(f'O valor inteiro digitado foi {inteiro} e o real foi {real}.')