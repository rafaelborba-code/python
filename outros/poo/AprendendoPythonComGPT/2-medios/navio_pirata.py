# Crie uma classe Pirata com os atributos nome, funcao e nivel_experiencia.
# Depois, crie uma classe NavioPirata que gerencia a tripulação e tem métodos para adicionar piratas e mostrar todos os piratas a bordo.

class Pirata:
    def __init__(self, nome, funcao, nivel_exp):
        self.nome = nome
        self.funcao = funcao
        self.nivel_exp = nivel_exp
        print(f'{self.nome} - {self.funcao} (Experiência: {self.nivel_exp})')


class NavioPirata:
    def __init__(self, navio):
        self.navio = navio
        self.tripulacao = []

    def adicionar_pirata(self, pirata):
        self.tripulacao.append(pirata)
        print(f'{pirata.nome} foi adicionado à tripulação do {self.navio}.')
    
    def mostrar_tripulacao(self):
        print(f'Tripulação do {self.navio}:')
        for pirata in self.tripulacao:
            print(f'{pirata.nome} - {pirata.funcao} (Experiência: {pirata.nivel_exp})')

def linha():
    print('-'*50)


navio_pirata = NavioPirata('Going Merry')
pirata1 = Pirata('Edward Newgate', 'Capitão', 1000)
pirata2 = Pirata('Barba Negra', 'Capitão', 750)
linha()
navio_pirata.adicionar_pirata(pirata1)
navio_pirata.adicionar_pirata(pirata2)
linha()
navio_pirata.mostrar_tripulacao()
