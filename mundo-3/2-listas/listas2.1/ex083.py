expressao = input('Digite uma expressão numérica: ')
pilha=[]
for caractere in expressao:
    if caractere == '(':
        pilha.append(caractere)
    if caractere == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(caractere)
            break#Não é necessário, está sendo usado apenas para economizar processamento
if len(pilha) == 0:
    print('Essa expressão é válida! ')
else:
    print('Essa expressão é inválida! ')