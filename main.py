#Notes
#If possible please keep the updateBackpack() before the updateHealth(), it just looks better, although I am working on having them "spawn in" if you will in better spots


#Imports
from visuals import healthBar, BackPack
import time
import os

#Defining functions for convinience 
#Just making things faster to call
def cls():
    os.system('cls')

def sleep(num=1): 
    #So if you just call sleep() with no parameters it will stop 1 second as the default, but you can also specify more if you want
    time.sleep(num)

#Initialising Values
backpack = BackPack
inputs = ["use", "take", "attack", "run", "ask", "tell", "look", "drop", "north", "south", "east", "west", "yes", "no", "exit"] #List of valid inputs
health = healthBar


#General Functions
def validateInput(inp): 
    #I suspect that this will have to be edited soon, but until then it's the idea that counts, you get it
    while inp not in inputs:
        if inp != "":
            print ("I'm sorry, I didn't quite understand that.")
            print ("Please try again")
        inp = input("> ")
    return inp

#Press Start
input("Press Enter To Start: ")
cls()
try:
    #All the Actual Code
    health.updateHealthBar(100)
    backpack.updateBackPack()
    print ("Introduction")
    inp = validateInput(input("> "))
    backpack.add("Burger")
    backpack.add("Dagger")
    backpack.updateBackPack()
    health.updateHealthBar(25)
    health.updateHealthBar(75, user=False)
    inp = validateInput(input("> "))
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
    sleep()
    cls()
    backpack.updateBackPack(finish=True)
    health.updateHealthBar(input("Press Enter To Finish The Game: "), finish=True)
    
