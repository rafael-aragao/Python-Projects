class Animal:
    def fazer_som(self):
        print("Som")


class Cachorro(Animal):
    def fazer_som(self):
        print("Latido")


class Gato(Animal):
    def fazer_som(self):
        print("Miau")


animais = [Cachorro(), Gato()]

for a in animais:
    a.fazer_som()