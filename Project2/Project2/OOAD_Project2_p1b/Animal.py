from abc import  ABC,abstractmethod
import RoamBehaviour

class Animal(ABC):
    def __init__(self):
        self.roambehaviour=RoamBehaviour
    def sleep(self):
        return "is sleeping"
    def wakeup(self):
        return " is  wakingup"
    # As part of the strategy pattern, the Animal delegates roaming responsibility to the Roamer. A RoamBehaviour class has been created for the behaviours of different species.
    def roam(self):
        return self.roambehaviour.roam(self)
#     // below abstract methods are implemented in their respective sub classes
    def eat(ABC):
        pass
    def makeNoise(ABC):
        pass
    def type(ABC):
        pass

    
    
    
    
    
    