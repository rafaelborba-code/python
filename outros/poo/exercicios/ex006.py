from math import pi

class Forma:
    def area(self):
        pass

class Circulo(Forma):
    def area(self, raio):
        return pi*(raio**2)
    

class Retangulo(Forma):
    def area(self, l, a):
        return l * a

circulo = Circulo()
retangulo = Retangulo()

print(circulo.area(3))
print(retangulo.area(5, 3))