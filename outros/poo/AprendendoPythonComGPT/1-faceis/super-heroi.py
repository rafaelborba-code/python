# Crie uma classe Heroi com os atributos nome, poder e cidade. 
# Adicione um método salvar_dia() que imprime uma mensagem do tipo: 🦸 "Superman usou Super Força para salvar Metrópolis!"

class Hero:
    def __init__(self, nome, poder, cidade):
        self.nome = nome
        self.poder = poder
        self.cidade = cidade

    def salvarDia(self):
        return f'🦸 {self.nome} usou {self.poder} para salvar {self.cidade}!'
    

superman = Hero('Superman', 'Olhos Laser', 'Metrópolis')
print(superman.salvarDia())