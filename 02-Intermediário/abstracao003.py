from abc import ABC, abstractmethod
import math

class FormaGeometrica(ABC):
    @abstractmethod
    def calcular_area(self):
        pass


class Retangulo(FormaGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura


class Triangulo(FormaGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return (self.base * self.altura) / 2


class Circulo(FormaGeometrica):
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return math.pi * self.raio ** 2


formas = [Retangulo(4, 5), Triangulo(3, 6), Circulo(2)]

for f in formas:
    print(f.calcular_area())