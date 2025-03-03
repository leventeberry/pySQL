from multiprocessing.spawn import set_executable

from initialize import showGreeting
from rich.console import Console
import questionary
import choices.mainMenuChoices as mainChoices

console = Console()
bkpoint = "\n////////////////////////////////////////////////////////////////////////////\n"

#Create Line Break Function
def newLineBk():
    console.print(f"[green]{bkpoint}[/green]")

def mainMenuOptions():
    newFunction = True

    while newFunction:
        selection = questionary.select(
            "Select an Option:",
            choices=[
                mainChoices.connectionConfig,
                mainChoices.testConfig,
                mainChoices.exitApp
            ]).ask()
        if selection == "q":
            newFunction = False
        elif selection == 1:
            print("User Selected 1")
        elif selection == 2:
            print("User Selected 2")

#Define main function
def main():
    showGreeting()
    newLineBk()
    mainMenuOptions()

#Start main function
main()
