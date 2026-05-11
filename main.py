from entities import Player
from colored import Fore, Style

pName = "" # Name Will be used throughout the game session
isPlaying = True # Game State

def intro():
    print(Fore.green + f"Welcome to Terminal RPG!" + Style.reset)
    print(Fore.cyan + f"==================================================" + Style.reset)
    print(Fore.green + f"Name your character: " + Style.reset)
    pName = input("> ")
    p1 = Player(pName)

    print(Fore.green + f"\nThe legend of {Fore.yellow + pName + Style.reset + Fore.green} begins..." + Style.reset)
    print(Fore.cyan + f"==================================================" + Style.reset)

actions = {
    1: encounter,
    2: inventory,
    3: shop,
    4: "End Game"
}

def action():
    print(Fore.green + f"What would {Fore.yellow + pName + Style.reset + Fore.green} like to do?" + Style.reset)
    print(Fore.cyan + f"==================================================" + Style.reset)
    
    print (Fore.green + f"1. {actions[1]}" + Style.reset)

def encounter():
    # Spawn enemy of difficulty choice, then fight until one of them dies.
    return 
def inventory():
    # Displays player's inventory 
    pass
def shop():
    # focus on combat system first, implementation later
    pass


# Game Loop

def main():
    intro()

    while isPlaying:
        action()