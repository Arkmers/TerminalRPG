from colored import Fore, Style

def printbar():
    print(Fore.cyan + f"==================================================" + Style.reset)

def expBar(Player):
    expPercentage = Player.experience / Player.maxExperience
    barLength = 20
    filledLength = int (barLength * expPercentage)
    bar = "[" + "#" * filledLength + "-" * (barLength - filledLength) + "]"
    print(Fore.cyan + f"EXP : " + Fore.yellow + f"{bar} {Player.experience}/{Player.maxExperience}" + Style.reset)
