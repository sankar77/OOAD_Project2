from Animal import *
# Roam Behaviour is the abstract class implemented by different concrete classes.all the different types of roam are embedded in this function.
class RoamBehaviour:
    def roam(self):
        pass
    

class CanineRoam(RoamBehaviour):
    def roam(self):
        return "is roaming fast"
    
    
class FelineRoam(RoamBehaviour):
    def roam(self):
        return "is roaming very fast"

class PachydermRoam(RoamBehaviour):
    def roam(self):
        return "is roaming slowly"
