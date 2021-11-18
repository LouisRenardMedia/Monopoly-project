import random 
import numpy
from datetime import datetime
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

pos=0
rep=200
class square:
    def __init__(self, name, index) -> None:
        self.name = name
        self.index=index
        self.gotojail = False
        self.counter=0
        self.injail=False
        self.jailcounter=0
        self.chances=False
    def enter (self):
        self.counter+=1
        #print (self.name)
    def statprint (self):
        #print (self.name+" "+str(self.counter*100/rep)+"%")
        print ("{:30}: {:2.2%}".format(self.name,self.counter/rep))
    def jail (self):
        return self.injail
    def jailturns (self):
        self.jailcounter+=1

class cards:
    def __init__(self, name, index) -> None:
        self.name = name
        self.index = index
        self.go = False
    def chance (self):
        return self.chances
    def go ()

cardnameschance = ["not1", "not2", "not3", "not4", "not5", "not6", "jail", "GO", "Trafalgar Square", "Mayfair", "pall mall", "near station 1", "near staion 2", "near utility", "back 3", "kings cross"]
chance= []

names = ["Go", "Old Kent Road", "Community", "Whitechapel Road", "income tax", "King's Cross station", "Chance", "The Angel Islington", "Euston Road", "Pentonville Road", "Visiting jail", "Pall Mall", "Electricity woks", "Whitehall", "Northumberland Avenue", "Marylebone station", "Bow Street", "Community 2", "Marlborough Street", "Vine Street", "Free parking", "The Strand", "Chance 2", "Fleet Street", "Trafalgar Square", "Fenchurch Street station", "Leicester Square", "Coventry Street", "Water works", "Piccadilly", "go to jail", "Regent Street", "Oxford Street", "Community 3", "Bond Street", "Liverpool Street station", "Chance 3", "Park Lane", "Super tax", "Mayfair", "Jail",]
squares = []

for name in names:
    squares.append(square(name, len(squares)))
squares [30].gotojail=True
squares [40].injail=True
squares [6].chances=True
#for case in squares:
    #print (case.name)
jailturn=0
for i in range(rep):
    [x,y]=roll_dice()
    #log.write("x:"+str(x)+",y:"+str(y))
    diceval= (x+y)
    if squares[pos].injail:
        squares[pos].enter()
        #log.write("jail:"+str(jailturn))
        if jailturn==2:
            pos=10+diceval
            jailturn=0
            #log.write("pos:"+str(pos))
        else:
            [x,y]=roll_dice()
            #log.write("x:"+str(x)+",y:"+str(y))
            if x==y:
                jailturn=0
                pos=10+x+y
            else :
                jailturn+=1
    else:
        pos+=diceval
        pos=pos%40
        if squares[pos].gotojail:
            pos=40
        else:
            if squares[pos].chances:
                #pick card and have effect
                print("yes")
            else:
                squares[pos].enter()
        
    
for i in squares:
    i.statprint()

log.close()