#Notes
#If possible please keep the updateBackpack() before the updateHealth(), it just looks better, although I am working on having them "spawn in" if you will in better spots


#Imports
from classes import healthBar, BackPack, character
import time
import os

#Defining functions for convenience 
#Just making things faster to call
def cls():
    os.system('cls')

def sleep(num=1): 
    #So if you just call sleep() with no parameters it will stop 1 second as the default, but you can also specify more if you want
    time.sleep(num)

#Initialising Values
backpack = BackPack
basicInputs = ["use", "take", "attack", "run", "ask", "tell", "look", "drop", "n", "s", "e", "w", "yes", "no"] #List of valid inputs
health = healthBar


#General Functions
def validateInput(inp, inputs=basicInputs): 
    #I suspect that this will have to be edited soon, but until then it's the idea that counts, you get it
    while inp not in inputs:
        if inp != "":
            print ("I'm sorry, I didn't quite understand that.")
            print ("Please try again")
        inp = input("> ")
    inp = inp[0].lower()
    return inp

def stonehill():
    cls()
    print("Welcome to the Stonehill Inn, the heart of the small town of Phandalin. This inn serves as a reststop for travellers making the long journey towards the Sword Mountains. \nNestled in the foothills of the Sword Mountains, Phandalin is a quaint little town, home to around 1000 people. It sits at the base of Icespire Peak, which is one of the highest peaks of the mountains. Atop of the summit sits the feared White Dragon of Icespire, who has overrun the Icespire Fort and periodically flies down to attack the village. \n ")
    input("Press enter to continue: ")
    cls()
    print("The Stonehill Inn has a rather modest interior, with wooden pillars haphazardly strewn across the floor, holding up the floor above, which holds the bedrooms. The innkeeper calls over to you and asks, \n'Oi! You! You look like a traveller. You heard of that Harvin Wester in town? He's the townmaster, and I heard he's looking for an adventurer to do some quests for him. Heard he's paying out big time!'")
    input("Press enter to continue: ")
    cls()
    input("Press enter to go outside: ")
    phandalinSquare()

def phandalinSquare():
    cls()
    print("Phandalin Square is, as you would experct of a small town, not too busy or big, though a few stalls line the outside. You see a sign pointing different ways in the centre of the square next to a fountain.")
    input("Press enter to investigate: ")
    cls()
    print("The sign has three points. The first, which points North, reads 'Triboar Trail'; the second, which points East, reads 'Townmaster's house', and the third, which points West, reads 'Gnomengarde'")
    print("Which way would you like to go? (n,e,s)")
    inp = validateInput(input(),inputs=["n","e","s"])
    if inp == "n":
        triboar()
    elif inp == "e":
        townmaster()
    elif inp == "s":
        gnomengarde()

def noticeBoard(inp, questGnome, questTri, questDragon):
    questGnome = False
    questTri = False
    questDragon = False
    if inp == "1":
        print("The first paper reads 'The King of Gnomengarde, Korboz, calls for help to the south of Phandalin. A mimic is terrorising their cave and it needs to be destroyed.'")
        input("Press enter to continue: ")
        questGnome = True
        return questGnome
    elif inp == "2":
        print("Manticore")
        input("Press enter to continue: ")
        questTri = True
        return questTri
    elif inp == "3":
        print("Dragon")
        input("Press enter to continue: ")
        return questDragon

def townmaster():
    print("You walk east from the main square towards Townmaster Harvin Wester's house. As you arrive at this house, there is a notice board outside, which has three pieces of paper on it. Which would you like to read? (1,2,3)")
    inp = validateInput(input(),inputs=["1","2","3"])
    noticeBoard(inp)

def triboar(questTri):
    if questTri != True:
        "Inactive Quest: returning to main square..."
        phandalinSquare()
    else:
        print("")
        


classList = ["Druid","Ranger","Barbarian","Paladin",]

classStats = [["Class","Race","Health","Weapon Name","AttackMin","AttackMax","Defense","Multiplier","Speed"],
              ["Druid","Elf",10,"Scimitar",1,6,13,1,35],
              ["Ranger","Elf",10,"Longbow",1,8,14,3,25],
              ["Barbarian","Elf",14,"Greataxe",1,12,14,2,15],
              ["Paladin","Elf",10,"Longsword",1,8,18,2,15],
              ]

#Press Start
input("Press Enter To Start: ")
cls()
try:
    #All the Actual Code
    user = character()
    health.updateHealthBar(100)
    backpack.updateBackPack()
    classChoice = ""
    while classChoice not in classList:
        cls()
        print("Class Options:")
        for i in classList:
            print(">",i)
        classChoice = input("Please select a class: ")
        classChoice = classChoice.title()

    cls()
    print("You have selected the",classChoice,"class!")
    row = 0
    if classChoice == "Druid":
        row = 1
    elif classChoice == "Ranger":
        row = 2
    elif classChoice == "Barbarian":
        row = 3
    elif classChoice == "Paladin":
        row = 4
    user.health = classStats[row][2]
    weaponName = classStats[row][3]
    user.attackMin = classStats[row][4]
    user.attackMax = classStats[row][5]
    user.defense = classStats[row][6]
    user.multiplier = classStats[row][7]
    user.speed = classStats[row][8]
    print("Your stats are: \nHealth:",user.health,"\nWeapon Name:",weaponName,"\nAttack: between",user.attackMin,"and",user.attackMax,"\nDefense:",user.defense,"\nSpeed:",user.speed)
    input("Press enter to continue: ")

    stonehill()

except Exception as e:
    print ("Sorry there's been an error, we'll restart")
    print (f"Error: {e}")
    input()
finally:
    #I need to keep this here
    #updateHealthBar(health) will not run unless there it is called afterwards again 
    #(and there is an input at some point in front of it)
    #This should allow it to keep being called as many times as I need 
    #It should also only run when the script is over or when there is an error
    cls()
    backpack.updateBackPack(finish=True)
    health.updateHealthBar(input("Press Enter To Finish The Game: "), finish=True)
    
