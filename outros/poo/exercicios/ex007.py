class Motor:
    def ligar(self):
        print('Motor ligado!')

class Carro:
    def __init__(self):
        self.motor = Motor()
    
    def ligar(self):
        self.motor.ligar()
        print('Carro ligado!')

carro = Carro()

carro.ligar()