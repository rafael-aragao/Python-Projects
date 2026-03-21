class Animal:
    def __init__(self, nome):
        self.nome = nome

    def emitir_som(self):
        print("Som genérico")

class Cachorro(Animal):
    pass


c = Cachorro("Rex")
c.emitir_som()