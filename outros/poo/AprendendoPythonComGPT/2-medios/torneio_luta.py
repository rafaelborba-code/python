# Crie uma classe Lutador com atributos nome, força e vida.
# Adicione um método atacar(outro_lutador) que reduz a vida do adversário com base na força do atacante.

class Lutador:
    def __init__(self, nome, forca, vida):
        self.nome = nome
        self.forca = forca
        self.vida = vida

    def atacar(self, oponente):
        oponente.vida -= self.forca
        print(f'{self.nome} atacou {oponente.nome} e causou {self.forca} de dano!')

    def mostrarVida(self):
        print(f'{self.nome} está com {self.vida} pontos de vida.')

l1 = Lutador('Bruce Lee', 50, 100)
l2 = Lutador('Bomba', 20, 120)
l1.atacar(l2)
l2.mostrarVida()