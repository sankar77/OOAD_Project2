from Animal import Animal
from abc import  ABC

class Canine(Animal,ABC):
    def type(self):
        return "Canine"
    def roam(self):
        return "is roaming fast"
    def eat(self):
        return "is eating Livestock"

