class Animal:
    def falar(self):
        pass

class Gato(Animal):
    def falar(self):
        print('O gato mia.')

class Cachorro(Animal):
    def falar(self):
        print('O cachorro late.')

gato = Gato()
cachorro = Cachorro()

gato.falar()
cachorro.falar()