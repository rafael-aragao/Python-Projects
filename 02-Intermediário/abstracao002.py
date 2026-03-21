from abc import ABC, abstractmethod

class Funcionario(ABC):
    @abstractmethod
    def calcular_salario(self):
        pass


class Horista(Funcionario):
    def __init__(self, horas, valor_hora):
        self.horas = horas
        self.valor_hora = valor_hora

    def calcular_salario(self):
        return self.horas * self.valor_hora


class Mensalista(Funcionario):
    def __init__(self, salario):
        self.salario = salario

    def calcular_salario(self):
        return self.salario


h = Horista(100, 20)
m = Mensalista(3000)

print(h.calcular_salario())
print(m.calcular_salario())