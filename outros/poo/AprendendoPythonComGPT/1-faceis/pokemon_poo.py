#Crie uma classe chamada Pokemon com os atributos nome, tipo e poder.
# Adicione um método atacar() que imprime uma mensagem do tipo: "Pikachu usou Choque do Trovão! Causou 50 de dano!"

ataques = {
    'elétrico': 'Choque do Trovão',
    'fogo': 'Lança-Chamas',
    'água': 'Jato d\'Água',
    'folha': 'Folha Navalha',
    'fantasma': 'Bola Sombria',
    'psíquico': 'Poder Psíquico',
    "lutador": "Soco Dinâmico",
    "pedra": "Deslize de Pedras",
    'terra': 'Terremoto'
}

class pokemon:
    def __init__(self, nome, tipo, dano):
        self.nome = nome
        self.ataque = ataques[tipo.lower()]
        self.dano = dano
    def atacar(self):
        print(f'{self.nome} usou {self.ataque}! Causou {self.dano} de dano!')

pikachu = pokemon('Nidoking', 'terra', 100)
pikachu.atacar()


