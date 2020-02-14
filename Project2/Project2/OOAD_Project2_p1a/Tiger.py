from Animal import Animal
from Feline import Feline
from abc import ABC

class Tiger(Feline):
    def __init__(self,name):
        self.name=name
        self.status=0
    def getName(self):
        return self.name
    def setStatus(self):
        self.status=1
    def getStatus(self):
        return self.status
    def makeNoise(self):
        return "is making sounds like prusten"