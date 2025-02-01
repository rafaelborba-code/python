class Veiculo:
    def __init__(self, modelo, ano):
        self.modelo = modelo
        self.ano = ano
    
    def ligar(self):
        print('O veículo está ligando.')

class Carro(Veiculo):
    def abastecer(self):
        print(f'O {self.modelo} está abastecendo.')

carro1 = Carro('Corsa', 2006)
carro1.ligar()
carro1.abastecer()