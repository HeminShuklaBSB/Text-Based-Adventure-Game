import tkinter as tk
import random
def doNothing():
    #Literally does nothing but please don't delete it 
    #It is used so that the user can't click exit 
    #Or alt f4 out of any of the widgets
    pass

def initialiseWindow(window, title, size): #Just made a function because it's used at least twice, might as well save some lines
    window.title(title)
    window.configure(background="black")
    window.minsize(size[0], size[1])
    window.maxsize(size[0], size[1])
    window.protocol("WM_DELETE_WINDOW", doNothing)

#Health Bar Section
class healthBar:
    healthBarWindow = tk.Tk() #Initialising the healthBarWindow
    healthBarWindow.protocol("WM_DELETE_WINDOW", doNothing)
    userHealth = 100

    def __init__(self):
        pass

    def updateHealthBar(health, user=True, finish=False): #Updates the visual health bar, for both the player and (if needed) the enemy who is represented in green
        if finish:
            exit()
        
        healthBar.healthBarWindow.destroy()
        healthBar.healthBarWindow = tk.Tk()
        if user:
            windowHeight = 100
            healthBar.userHealth = health
        else:
            windowHeight = 170

        initialiseWindow(healthBar.healthBarWindow, "Health Bar", (500, windowHeight))
        healthBarMain = tk.Canvas(healthBar.healthBarWindow, width=500, height=windowHeight, bg="black")
        healthBarMain.create_rectangle(50, 30, 450, 70, fill="gray")
        healthBarMain.create_rectangle(50, 30, 50 + healthBar.userHealth * 4, 70, fill="red")
        if not user:
            healthBarMain.create_rectangle(50, 100, 450, 140, fill="gray")
            healthBarMain.create_rectangle(50, 100, 50 + health * 4, 140, fill="green")

        healthBarMain.pack()
        



#Backpack Section
class BackPack:
    backpack = []
    backpackWindow = tk.Tk()
    backpackWindow.protocol("WM_DELETE_WINDOW", doNothing) #Stops the user from being able to alt f4 or click exit on the widget to prevent errors
    def __init__(self):
        pass
    
    def updateBackPack(finish=False): #Updates the visual list of what the backpack contains
        if finish: #Does nothing if called at the end
            pass
        else:
            BackPack.backpackWindow.destroy()
            BackPack.backpackWindow = tk.Tk()
            initialiseWindow(BackPack.backpackWindow, "Backpack Contents", (200, 800))
            tk.Label(BackPack.backpackWindow, anchor="center", text="Items:", bd=0, bg="black", fg="lightGray", font="MS 30").pack()
            if len(BackPack.backpack) == 0:
                tk.Label(BackPack.backpackWindow, anchor="w", text="You Have No Items To Display!", bd=0, bg="black", fg="lightGray", font="MS 10").pack()
            else:
                for i in range(len(BackPack.backpack)):
                    tk.Label(BackPack.backpackWindow, anchor="w", text=f"- {BackPack.backpack[i]}", bd=0, bg="black", fg="lightGray", font="MS 20").pack()
            

    def add(item):
        BackPack.backpack.append(item) #Adds an item to the backpack
    
    def remove(item):
        try:
            BackPack.backpack.remove(item) #Removes an item from the backpack
        except Exception as e:
            print ("Sorry, there was an error, we're going to have to restart") #To make debugging easier/looks better if it doesn't just crash 
            print (f"Error: {e}")


class character:
    def __init__(self, health=100, attack=10, defense=10, specialAttacks=False, multiplier=0):
        self.health = health
        self.attack = attack + multiplier
        self.defense = defense
        self.specialAttacks = specialAttacks
        self.multiplier = multiplier


def attack(user, character)