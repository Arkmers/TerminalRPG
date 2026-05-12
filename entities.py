from colored import Fore, Style
from helper import printbar
from helper import expBar

class Player:
    def __init__ (self, name, maxHitpoints = 10, level = 1, experience = 0, attack = 2, defense = 1, inventory = [], gold = 0):

        self.name = name
        
        self.level = 1
        self.experience = 24
        self.maxExperience = 100

        self.attack = attack
        self.defense = defense
        self.maxHitpoints = maxHitpoints
        self.hitpoints = maxHitpoints

        self.inventory = []
        self.gold = 0
        
    def display_stats(self):
        
        printbar()
        print(Fore.green + f"{self.name}'s Stats:" + Style.reset)
        print(Fore.cyan + f"LVL : {self.level}" + Style.reset)
        expBar(self)
        print("")
        print(Fore.cyan + f"HP  : {self.hitpoints}/{self.maxHitpoints}" + Style.reset)
        print(Fore.cyan + f"ATK : {self.attack}" + Style.reset)
        print(Fore.cyan + f"DEF : {self.defense}" + Style.reset)

    def display_inventory(self):

        printbar()
        print(Fore.green + f"{self.name}'s Inventory:" + Style.reset)

        if self.inventory:
            for item in self.inventory:
                print(Fore.cyan + f"- {item}" + Style.reset)
        else:
            print(Fore.cyan + "Your inventory is empty." + Style.reset)
        printbar()

class Enemy:
    def __init__ (self, name, maxHitpoints, attack, defense, experienceReward, goldReward, itemReward):
        self.name = name
        self.maxHitpoints = maxHitpoints
        self.hitpoints = maxHitpoints
        self.attack = attack
        self.defense = defense
        self.experienceReward = experienceReward
        self.goldReward = goldReward
        self.itemReward = itemReward

    