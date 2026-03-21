class Veiculo:
    def __init__(self, velocidade):
        self.velocidade = velocidade

    def mover(self):
        print(f"Movendo a {self.velocidade} km/h")


class Carro(Veiculo):
    pass


class Moto(Veiculo):
    pass


c = Carro(100)
m = Moto(80)

c.mover()
m.mover()