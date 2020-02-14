from ZooKeeper import ZooKeeper
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

if __name__=="__main__":
    Cody = Cat("Cody");
    Code =  Cat("Code");
    Code.setStatus()
    Donald =  Dog("Donald");
    Dash =  Dog("Dash");
    Dash.setStatus();
    Eric =  Elephant("Eric");
    Edward =  Elephant("Edward");
    Edward.setStatus();
    Heman =  Hippo("Heman");
    Heather =  Hippo("Heather");
    Heather.setStatus();
    Luke =  Lion("Luke");
    Lisa =  Lion("Lisa");
    Lisa.setStatus();
    Rosy = Rhino("Rosy");
    Rambo = Rhino("Rambo");
    Rambo.setStatus();
    Todd =  Tiger("Todd");
    Toby =  Tiger("Toby");
    Toby.setStatus();
    William =  Wolf("William");
    Watson =  Wolf("Watson");
    Watson.setStatus();
    list1=[]
#     Adding the list of all the animals to a list
    list1.append(Cody);
    list1.append(Code);
    list1.append(Donald);
    list1.append(Dash);
    list1.append(Eric);
    list1.append(Edward);
    list1.append(Heman);
    list1.append(Heather);
    list1.append(Luke);
    list1.append(Lisa);
    list1.append(Rosy);
    list1.append(Rambo);
    list1.append(Todd);
    list1.append(Toby);
    list1.append(William);
    list1.append(Watson);
    z=ZooKeeper();
    print("---------Opening the zoo---------");
# //        zoo keeper opening the zoo
    z.openZoo();

    print("----------Roll calling the animals-------");
# //        zoo keeper roll calling all the animals in the zoo
    z.rollCallAnimals(list1);

    print("-------Wakeup the Animals-----------");
# //        zoo keeper waking up the animals in the zoo
    z.wakeAnimals(list1);

    print("----------Feeding the Animals------------");
# //        zoo keeper feeding the Animals in the zoo
    z.feedTheAnimals(list1);
    print("----------Exercise The Animals-------------");
# //        zoo keeper making the animals in the zoo to exercise
    z.exerciseTheAnimals(list1);
    print("----------Random Behaviour in Cat-----------");
# //        cat random behavior
    Code.randombehav();
    print("---------Shutting Down the Zoo---------------");
# //        zoo keeper shutting the zoo
    z.shutZoo();


