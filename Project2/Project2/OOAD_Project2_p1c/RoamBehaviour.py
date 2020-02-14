from Animal import *

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
