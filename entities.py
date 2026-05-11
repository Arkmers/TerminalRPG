from colored import Fore, Style

class Player:
    def __init__ (self, name, health=10, level=1, experience=0, atk = 2, defense = 1):

        self.name = name
        
        self.__level = 1
        self.__experience = 0

        self.__atk = atk
        self.__defense = defense
        self.__health = health

        self.__inventory = []
        
    def display_stats(self):
        
        print(Fore.green + f"{self.name}'s Stats:" + Style.reset)
        print(Fore.cyan + f"Health: {self.health}" + Style.reset)
        print(Fore.cyan + f"Level: {self.level}" + Style.reset)
        print(Fore.cyan + f"Experience: {self.experience}" + Style.reset)
    
    def display_inventory(self):

        print(Fore.green + f"{self.name}'s Inventory:" + Style.reset)

        if self.inventory:
            for item in self.inventory:
                print(Fore.cyan + f"- {item}" + Style.reset)
        else:
            print(Fore.cyan + "Your inventory is empty." + Style.reset)
