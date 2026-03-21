class Funcionario:
    def __init__(self, salario):
        self.salario = salario

    def calcular_bonus(self):
        return self.salario * 0.1


class Gerente(Funcionario):
    def calcular_bonus(self):
        return self.salario * 0.2


class Programador(Funcionario):
    def calcular_bonus(self):
        return self.salario * 0.15


g = Gerente(5000)
p = Programador(4000)

print(g.calcular_bonus())
print(p.calcular_bonus())