import math

class Forma:
    def calcular_area(self):
        pass


class Quadrado(Forma):
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado ** 2


class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return math.pi * self.raio ** 2


formas = [Quadrado(4), Circulo(3)]

for f in formas:
    print(f.calcular_area())