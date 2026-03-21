class Produto:
    def __init__(self, preco):
        self._preco = preco

    def set_preco(self, novo_preco):
        if novo_preco > 0:
            self._preco = novo_preco
        else:
            print("Preço inválido")

    def get_preco(self):
        return self._preco


p = Produto(50)
p.set_preco(100)
print(p.get_preco())