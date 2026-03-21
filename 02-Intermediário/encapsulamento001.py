class Pessoa:
    def __init__(self):
        self._idade = 0

    def set_idade(self, idade):
        if idade >= 0:
            self._idade = idade
        else:
            print("Idade inválida")

    def get_idade(self):
        return self._idade


p = Pessoa()
p.set_idade(20)
print(p.get_idade())