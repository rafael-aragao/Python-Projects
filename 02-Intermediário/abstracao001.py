from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def fazer_som(self):
        pass


class Cachorro(Animal):
    def fazer_som(self):
        print("Latido")


c = Cachorro()
c.fazer_som()