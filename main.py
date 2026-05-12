from entities import Player
from colored import Fore, Style
from helper import printbar

isPlaying = True # Game State
pName = "" # Player Name
global player
def intro():
    global player
    characterCreated = False
    attempts = 0
    
    print(Fore.green + f"Welcome to Terminal RPG!" + Style.reset)
    printbar()
    while characterCreated == False:
        print(Fore.green + f"Name your character: " + Style.reset)
        pName = input("> ").strip()
        
        if pName != "":
            characterCreated = True
            
            player = Player(pName)
            print(Fore.green + f"\nThe legend of {Fore.yellow + pName + Style.reset + Fore.green} begins..." + Style.reset)
            printbar()
            
        elif (pName == "" and attempts == 5):
            print(Fore.red + f"You are now Nameless." + Style.reset)
            characterCreated = True
            pName = "Nameless One"
            player = Player(pName)
            print(Fore.green + f"\nThe legend of the {Fore.red + pName + Style.reset + Fore.green} begins..." + Style.reset)
            printbar()
        else:
            print(Fore.red + f"Invalid name. Please try again." + Style.reset)
            attempts += 1


def encounter(Player):
    # Spawn enemy of difficulty choice, then fight until one of them dies.
    pass

def inventory(Player):
    # Display Stats and Inventory
    Player.display_stats()
    Player.display_inventory()
    return True

def shop(Player):
    # focus on combat system first, implementation later
    pass

def end(Player):
    printbar()
    print(Fore.green + f"Thank you for playing Terminal RPG!" + Style.reset)
    return False

actions = {
    "1": encounter,
    "2": inventory,
    "3": shop,
    "4": end
}

def action(Player):
    print(Fore.green + f"What would {Fore.yellow + Player.name + Style.reset + Fore.green} like to do?" + Style.reset)
    printbar()
    
    print(Fore.green + f"1. Encounter" + Style.reset)
    print(Fore.green + f"2. Inventory" + Style.reset)
    print(Fore.green + f"3. Shop" + Style.reset)
    print(Fore.green + f"4. End Game" + Style.reset)
    printbar()
    choice = input("> ").strip()
    if choice in actions:
        result = actions[choice](player)
        if result is False:
            global isPlaying
            isPlaying = False
    else:
        print(Fore.red + f"Invalid choice. Please try again.\n" + Style.reset)

# Game Loop

def main():
    intro()

    while isPlaying:
        action(player)

main()