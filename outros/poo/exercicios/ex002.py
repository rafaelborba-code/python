class ContaBancaria:
    def __init__(self, saldo, titular):
        self.saldo = saldo
        self.titular = titular
    
    def depositar(self, valor):
        self.saldo += valor
        print(f'R${valor} depositados com sucesso!')

    def sacar(self, valor):
        self.saldo -= valor
        print(f'R${valor} sacados com sucesso!')

    def ver_saldo(self):
        return self.saldo

conta = ContaBancaria(15000, 'Rafael')
conta.depositar(5000)
conta.sacar(10000)
print(conta.ver_saldo())