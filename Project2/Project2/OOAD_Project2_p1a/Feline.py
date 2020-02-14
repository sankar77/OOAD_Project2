from Animal import Animal
from abc import  ABC

class Feline(Animal,ABC):
    def type(self):
        return "Feline"
    def roam(self):
        return "is roaming very fast"
    def eat(self):
        return "is eating meat"
