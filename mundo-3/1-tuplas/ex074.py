from random import randint
def forma_1():
    nums = (
        randint(0,9), 
        randint(0,9), 
        randint(0,9), 
        randint(0,9), 
        randint(0,9)
    )
    crescente = sorted(nums)
    print(f'Os valores sorteados foram: ',end='')
    for n in nums:
        print(n, end=' ')
    print(f'\nO maior valor sorteado foi {crescente[-1]}')
    print(f'O menor valor sorteado foi {crescente[0]}')

def forma_2():
    nums = (
        randint(0,9), 
        randint(0,9), 
        randint(0,9), 
        randint(0,9), 
        randint(0,9)
    )
    print(f'Os valores sorteados foram: ',end='')
    for n in nums:
        print(n, end=' ')
    print(f'\nO maior valor sorteado foi {max(nums)}')
    print(f'O menor valor sorteado foi {min(nums)}')
forma_2()