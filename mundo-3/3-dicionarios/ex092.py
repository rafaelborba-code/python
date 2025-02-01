from datetime import date
info = {}

atual = date.today().year
nome = input('Nome: ')
ano_nasc = int(input('Ano de nascimento: '))
idade = atual - ano_nasc
carteira_trabalho = int(input('Carteira de Trabalho (0 não tem) : '))
info['Nome'] = nome
info['Idade'] = idade
info['CTPS'] = carteira_trabalho
if carteira_trabalho != 0:
    ano_contrato = int(input('Ano de contratação: '))
    salario = float(input('Salário: R$'))
    info['Contratação'] = ano_contrato
    info['Salário'] = salario
    info['Aposentadoria'] = idade + (35 - (atual - ano_contrato))

print('-='*20)
for k, v in info.items():
    print(f' - {k} = {v}')