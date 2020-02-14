from zookeeper import *
from Animal import *
from Canine import *
from Pachyderm import *
from Feline import *
from Cat import *
from Dog import *
from Elephant import *
from Hippo import *
from Rhino import *
from Lion import *
from Tiger import *
from Wolf import *

class zookeeper:
    def openZoo(self):
        print("Zoo is opened")
    
    def rollCallAnimals(self,Animals):
        for i in range(len(Animals)):
            c=Animals[i].getStatus()
            if c==1:
                print(Animals[i].getName()+" "+"is present in the zoo")
            else:
                print(Animals[i].getName()+" "+"is present in the zoo")
    
    def wakeAnimals(self,Animals):
        for i in range(len(Animals)):
            c=Animals[i].getStatus()
            if c==1:
                print(Animals[i].getName()+" "+ Animals[i].wakeup())
    
    def feedTheAnimals(self,Animals):
        for i in range(len(Animals)):
            c=Animals[i].getStatus()
            if (c==1):
                print(Animals[i].getName()+" "+ Animals[i].eat());
                
    def exerciseTheAnimals(self,Animals):
        for i in range(len(Animals)):
            c=Animals[i].getStatus()
            if (c==1):
                print(Animals[i].getName()+" "+ Animals[i].roam()) 
                
    def shutZoo(self):
        print("Zoo is shutdown")
        
