from datetime import date

def voto(i):
    if i < 16:
        return 'NÃO VOTA'
    if 16 <= i < 18 or i > 70:
        return 'VOTO OPCIONAL' 
    if i > 17 and i < 70:
        return 'VOTO OBRIGATÓRIO'


ano_nasc = int(input('Ano de nascimento: '))
idade = date.today().year - ano_nasc
print(f'Com {idade} anos: {voto(idade)}')