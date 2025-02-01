def numeric_input(question):
    while True:
        n = input(question)
        if n.isnumeric() == False:
            print('\033[31mERRO! Digite um número inteiro válido. \033[m')
        else:
            return n


num = numeric_input('Digite um número: ')
print(f'Você acabou de digitar o número {num}')