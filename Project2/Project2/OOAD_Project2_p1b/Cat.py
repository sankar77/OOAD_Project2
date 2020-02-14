from Animal import *
from Feline import Feline
import random 
from RoamBehaviour import FelineRoam

class Cat(Feline):
    def __init__(self,name):
        self.name=name
        self.status=0
        self.roambehaviour=FelineRoam
    
    def getName(self):
        return self.name
    def setStatus(self):
        self.status=1
    def getStatus(self):
        return self.status
    def makeNoise(self):
        return "is making sounds like meow"
    def randombehav(self):
        rand=random.randint(0,4)
        rand=rand+1
        if rand==1:
            print(self.getName()+" "+self.sleep())
        elif rand==2:
            print(self.getName()+" "+self.eat())
        elif rand==3:
            print(self.getName()+" "+self.wakeup())
        elif rand==4:
            print(self.getName()+" "+self.makeNoise())
        elif rand==5:
            print(self.getName()+" "+self.roam())         
        
        
