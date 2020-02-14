from abc import  ABC,abstractmethod
import RoamBehaviour

class Animal(ABC):
#     In this zoo keeper is considered as the subject and zooAnnouncer is the observer.so we implemented two interfaces ZookeeperInterfaces 
# and zooAnnouncer Interface
    
    def __init__(self):
        self.roambehaviour=RoamBehaviour
    def sleep(self):
        return "is sleeping"
    def wakeup(self):
        return " is  wakingup"
    def roam(self):
        return self.roambehaviour.roam(self)
    def eat(ABC):
        pass
#     def roam(ABC):
#         pass
    def makeNoise(ABC):
        pass
    def type(ABC):
        pass

    
    
    
    
    
    