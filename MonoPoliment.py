import random 
import numpy 
from datetime import datetime

from numpy.lib.function_base import append
class log:
    def  __init__(self, filename):
        self.file = open(filename,'a+')
        self.write("Start log at " + datetime.now().strftime("%H:%m:%S"))
    def write(self,message):
        self.file.write(message + "\n")
    def close(self):
        self.file.close()
log=log ("log.txt")
def roll_dice():
    x = random.randint(1, 6)
    y = random.randint(1, 6)
    return [x,y]
def pick (tab):
        subs=random.choice(tab)
        tab.remove(subs)
        return subs
def Shuffle (tab):
    tabshuffle=[]
    while len(tab) != 0:
        tabshuffle.append(pick(tab))
    return tabshuffle

def pickPremsMeDer (tab):
    card=tab.pop(0)
    tab.append(card)
    return card

pos=0
rep=10000000
class square:
    def __init__(self, name, index):
        self.name = name
        self.index=index
        self.gotojail = False
        self.counter=0
        self.injail=False
        self.jailcounter=0
        self.chances=False
        self.community=False
    def enter (self):
        self.counter+=1
        #print (self.name)
    def statprint (self):
        #print (self.name+" "+str(self.counter*100/rep)+"%")
        print ("{:30}: {:2.2%}".format(self.name,self.counter/rep))
    def jail (self):
        return self.injail


class card:
    def __init__(self, name, target):
        self.name = name
        self.target = target
        self.move = target != 100
    def go (self):
        global pos
        if self.move:
            if self.target>=0:
                pos=self.target
            else:
                pos+=self.target
                if pos < 0:
                    pos+=40

class proxCard (card):
    def __init__(self, name, targets):
        super().__init__(name,0)
        self.targets = targets
    def go (self):
        global pos
        for target in self.targets:
            if target>pos:
                pos=target
                return
        pos=self.targets[0]


chanceshuffled = []
chance= [card("not1",100), card("not2",100), card("not3",100), card("not4",100), card("not5",100), card("not6",100), card("jail",40), card("GO",0), card("Trafalgar Square",24),card("Mayfair",39), card("pall mall",11), proxCard("near station 1",[5,15,25,35]),proxCard("near station 2",[5,15,25,35]), proxCard("near utility",[12,28]), card("back 3",-3), card("kings cross",5)]
communiti=[card("not01",100),card("not02",100),card("not03",100),card("not04",100),card("not05",100),card("not06",100),card("not07",100),card("not08",100),card("not09",100),card("not010",100),card("not011",100),card("not012",100),card("not013",100),card("not014",100),card("GO",0),card("jail",40),]
chanceshuffled = Shuffle (chance)
communitiShuffled = Shuffle(communiti)

names = ["Go", "Old Kent Road", "Community", "Whitechapel Road", "income tax", "King's Cross station", "The Angel Islington", "Chance", "Euston Road", "Pentonville Road", "Visiting jail", "Pall Mall", "Electricity woks", "Whitehall", "Northumberland Avenue", "Marylebone station", "Bow Street", "Community 2", "Marlborough Street", "Vine Street", "Free parking", "The Strand", "Chance 2", "Fleet Street", "Trafalgar Square", "Fenchurch Street station", "Leicester Square", "Coventry Street", "Water works", "Piccadilly", "go to jail", "Regent Street", "Oxford Street", "Community 3", "Bond Street", "Liverpool Street station", "Chance 3", "Park Lane", "Super tax", "Mayfair", "Jail",]
squares = []

for name in names:
    squares.append(square(name, len(squares)))
squares [30].gotojail=True
squares [40].injail=True
squares [7].chances=True
squares [22].chances=True
squares [36].chances=True
squares [2].community=True
squares [17].community=True
squares [23].community=True
#for case in squares:
    #print (case.name)
jailturn=0
doubleturn=0
for i in range(rep):
    [x,y]=roll_dice()
    #log.write("x:"+str(x)+",y:"+str(y))
    diceval= (x+y)
    if x==y:
        doubleturn+=1
    else:
        doubleturn=0
    if squares[pos].injail:
        squares[pos].enter()
        #log.write("jail:"+str(jailturn))
        if jailturn==2:
            pos=10+diceval
            jailturn=0
            doubleturn=0
            #log.write("pos:"+str(pos))
        else:
            #log.write("x:"+str(x)+",y:"+str(y))
            if x==y:
                jailturn=0
                doubleturn=0
                pos=10+x+y
            else :
                jailturn+=1
    else:
        if doubleturn ==3:
            pos=40
        else:
            pos+=diceval
            pos=pos%40
            if squares[pos].gotojail:
                pos=40
            elif squares[pos].chances:
                #pick card and have effect
                pickPremsMeDer(chanceshuffled).go()
                squares[pos].enter()
            elif squares[pos].community:
                #pick card and have effect
                pickPremsMeDer(communitiShuffled).go()
                squares[pos].enter()
            else:
                squares[pos].enter()
        
    
for i in squares:
    i.statprint()

log.close()