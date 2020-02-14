from Animal import Animal
from Pachyderm import Pachyderm
from abc import ABC

class Elephant(Pachyderm):
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
        return "is making trumphet noise"