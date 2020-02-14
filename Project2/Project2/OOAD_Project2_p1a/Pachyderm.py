from Animal import Animal
from abc import  ABC

class Pachyderm(Animal,ABC):
    def type(self):
        return "pachyderm"
    def roam(self):
        return "is roaming slowly"
    def eat(self):
        return "is eating grass"