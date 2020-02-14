from Animal import Animal
from Canine import Canine
from abc import ABC
from RoamBehaviour import CanineRoam

class Wolf(Canine):
    def __init__(self,name):
        self.name=name
        self.status=0
        self.roambehaviour=CanineRoam
    def getName(self):
        return self.name
    def setStatus(self):
        self.status=1
    def getStatus(self):
        return self.status
    def makeNoise(self):
        return "is making sounds like whimpering"