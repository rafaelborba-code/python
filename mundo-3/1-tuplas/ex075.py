nums = (int(input('Digite um número: ')),
        int(input('Digite outro número: ')),
        int(input('Digite mais um número: ')),
        int(input('Digite o último número: ')))
print(f'Os valores digitados foram: {nums}')
if nums.count(9) > 0:
    print(f'O valor 9 apareceu {nums.count(9)} vezes.')
else: 
    print('Não apareceu nenhum número 9 nas respostas.')

if nums.count(3) > 0:
    print(f'O primeiro número 3 apareceu na {nums.index(3)+1}ª posição.')
else:
    print('Não apareceu nenhum número 3 nas respostas.')

print('Valores pares que apareceram na resposta:', end=' ' )
cont_pares = 0
for n in nums:
    if n % 2 == 0:
        print(n, end=', ')
        cont_pares += 1
if cont_pares < 1:
    print('nenhum.')