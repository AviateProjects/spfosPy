# Made By Oliver W. 7-21-22 at github.coom/AviateProjects 

#Olivers library for Terminal App Production (OLTAP)
#start

#Stack mannegment (stackman)
rel=None 
runing=True

def ldr(functionName):
    global rel
    rel=functionName

def reloc():
    if rel is None:
        ldr(start)
    else:
        rel()

#List And Select Nodes And Subroutines (Travelman)

def stdLister(pretext,items):
    i=0
    print("\n"+pretext)
    while (i<len(items)):
        print(str(i)+": "+items[i])
        i+=1

def swan(pretext,items): #Switch Between An only Node List
    s=int(input(pretext))
    if(s>(len(items)-1)):
        global runing
        runing=False
    else:
        ldr(items[s])

def swos(pretext,items): #Switch Only Subroutines
    s=int(input(pretext))
    if(s>(len(items)-1)):
        global runing
        runing=False
    else:
        items[s]()

def mixSwitch(pretext,lookup,items):
    s=int(input(pretext))
    if(s>(len(items)-1)):
        global runing
        runing=False
    elif(lookup[s]):
        ldr(items[s])
    elif(not lookup[s]):
        items[s]()

#How to use Mixswitch
#mixSwitch("HI",(True,False,False),(Node,sbr,sbr))
#looup is a tupel of bools where True indicates a node and false indacates a subroutine

#end

import random as rand

#Initilizing Variables
shipName=""
name=""

hp=128
strength=16
ammo=32
cash=256

score=0


def main():
    while(runing):
        reloc()
    quit()

def start():
    Items=("Start","Info","Quit")
    stdLister("Space Pirates: From Outer Space! \n A game by Oliver W.",Items)
    swan("Select: ",(story,info))
def story():
    buffer=None
    i=0
    storLine=["","","","",""]
    storLine[0]="The Year Is 2113 The Height Of Spaceflight Traffic in the West Quandrent of the Galaxy"
    storLine[1]="Among one of Vessels a group with intent of taking the ship for there own sneaks Abord"
    storLine[2]="Then in the middle of the Voyage Somewhere between Rigel and Sirus \n a lound boom is heard acroos the vesel"
    storLine[3]="The Main surveailence system goes ofline \n The Crew is taken by Suprise and the group take the ship as there own"
    storLine[4]="Now its up to you Traveler will you take these vast expanses as your own \n and counquer the West Qudrant"
    while i is not (len(storLine)):
        print("\n"+storLine[i])
        buffer=input("\n Press ENTER to continue: ")
        i+=1
    ldr(init)
def info():
    print("\n version alpha 1 7-21-22")
    print("made by Oliver W.")
    ldr(start)

def init():
    print("All storys have a begining")
    global shipName,name
    name=input("What is your name Captin?: ")
    shipName=input("What shall you call your ship?:")
    print("\n You: "+name+" of The "+shipName+" goal is to fight and conquer across the galaxy ")
    ldr(center)


shipList=("The Atlas","The Ares","The Queen Elizibeth the 2nds Revenge","The Ranger","The Saturn IX","The Lone Star","The Adventurer","The Edison","The Luna 21")
def center():
    global avaInd
    avaInd=["","","","","",""]
    for i in range(6):
        global shipList
        avaInd[i]=shipList[rand.randint(0,7)]
    items=("Genral Store","Fight: "+avaInd[0],"Fight: "+avaInd[1],"Fight: "+avaInd[2],"Fight: "+avaInd[3],"Fight: "+avaInd[4],"Fight: "+avaInd[5],"Retire")
    stdLister("Hello Traveler what would you like to Do: ",items)
    
    global centSelect
    centSelect=int(input("Select: "))
    if centSelect is 0:
        ldr(trade)
    elif centSelect is 1 or 2 or 3 or 4 or 5 or 6:
        ldr(stat)
    else:
        quit()
def trade():
    global hp,strength,ammo,cash
    items=("Repair: 32 cash","Upgrade: 64 cash","buy ammo: 8 per","exit")
    stdLister("Avalibal options: ",items)
    s=int(input("Select: "))
    if cash>0:
        if s is 0:
            cash-=32
            hp+=64
        if s is 1:
            strength+=16
            cash-=64
        if s is 2:
            j=int(input("how much amo would you like to buy: "))
            cash-=(8*j)
            ammo+=j
        if s >= 3:
            ldr(center)
    else:
        print("You have no money get out! ")
        ldr(center)
def score():
    print("Your score is "+str(score))
    quit()
def stat():
    global avaInd, centSelect, shipList
    global hp,strength,ammo
    global opHp, opStr, opAmo, opCash
    opHp=rand.randint(hp-16,hp+16)
    opStr=rand.randint(strength-16,strength+8)
    opAmo=rand.randint(ammo-4,ammo+6)
    opCash=rand.randint(32,96)

    print("stats")
    print(shipName+" vs "+avaInd[centSelect-1])
    print("You have "+str(ammo)+" ammo")
    print("They have have "+str(opAmo)+" ammo")
    print("You have "+str(hp)+" hp")
    print("They have "+str(opHp)+" hp")
    print("you have "+ str(strength) +" strength")
    print("They have "+ str(opStr)+" strenth")
    print("They have "+ str(opCash) +" money abord")

    swan("Do you wish to engage? (1 for yes): ",(center,battle))
def battle():
    global avaInd, centSelect, shipList
    global hp,strength,ammo
    global opHp, opStr, opAmo, opCash
    global inBattle
    inBattle=True
    while(inBattle):
        if hp <= 0:
            score()
        elif opHp <= 0:
            win()
        elif ammo <= 0:
            print("You run out of amo and are forced to retreat")
            ldr(center)
            inBattle=False
        elif opAmo <= 0:
            print("They ran out of ammo")
            win()
        else:
            items=("engage","retreat")
            stdLister("Atack options: ",items)
            s=int(input("Select: "))
            if s is 0:
                opHp-=(strength*2)
                ammo-=1
                print("you atack "+str(strength*2)+" health taken away")
                print("They atack "+str(opStr*2)+" heath taken away")
                hp-=(opStr*2)
                opAmo-=1
            else:
                print("You retreat")
                inBattle=False
    ldr(center)


def win():
    global hp,strength,ammo,cash
    global opHp, opStr, opAmo, opCash
    global inBattle
    global score
    ammo+=opAmo
    cash+=opCash
    ldr(center)
    print("Battle Won with "+str(hp)+" hp!")
    inBattle=False
    score+=1
main()