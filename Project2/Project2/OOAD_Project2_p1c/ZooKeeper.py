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
from ZooKeeperInterface import *

class ZooKeeper(ZooKeeperInterface):
    def __init__(self):
        self.zlist=[]
    def openZoo(self):
        self.notifyZooAnnouncer("Zookeeper is opening Zoo")
        print("Zoo is opened")
    
    def rollCallAnimals(self,Animals):
        self.notifyZooAnnouncer("Zookeeper is roll calling Animals")
        for i in range(len(Animals)):
            c=Animals[i].getStatus()
            if c==1:
                print(Animals[i].getName()+" "+"is present in the zoo")
            else:
                print(Animals[i].getName()+" "+"is present in the zoo")
    
    def wakeAnimals(self,Animals):
        self.notifyZooAnnouncer("Zookeeper is waking Animals")
        for i in range(len(Animals)):
            c=Animals[i].getStatus()
            if c==1:
                print(Animals[i].getName()+" "+ Animals[i].wakeup())
    
    def feedTheAnimals(self,Animals):
        self.notifyZooAnnouncer("Zookeeper is feeding Animals")
        for i in range(len(Animals)):
            c=Animals[i].getStatus()
            if (c==1):
                print(Animals[i].getName()+" "+ Animals[i].eat());
                
    def exerciseTheAnimals(self,Animals):
        self.notifyZooAnnouncer("Zookeeper is exercising Animals")
        for i in range(len(Animals)):
            c=Animals[i].getStatus()
            if (c==1):
                print(Animals[i].getName()+" "+ Animals[i].roam()) 
                
    def shutZoo(self):
        self.notifyZooAnnouncer("Zookeeper is shutting down");
        print("Zoo is shutdown")
        
    def registerZooAnnouncer(self,za):
        self.zlist.append(za)
    
    def unRegisterZooAnnouncer(self,za):
        self.zlist.remove(za)
    
    def notifyZooAnnouncer(self,announcement):
        print(announcement)
        
        
