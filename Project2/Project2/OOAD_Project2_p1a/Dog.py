from Animal import Animal
from Canine import Canine
from abc import ABC

class Dog(Canine):
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
        return "is making sounds like meow"
    
    
