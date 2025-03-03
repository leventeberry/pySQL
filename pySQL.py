from initialize import showGreeting
from rich.console import Console
import questionary

console = Console()
bkpoint = "\n////////////////////////////////////////////////////////////////////////////\n"

#Create Line Break Function
def newLineBk():
    console.print(f"[green]{bkpoint}[/green]")

def mainMenuOptions():
    questionary.select(
        "Select an Option:",
        choices=[
            "[1]Configure Database Connection",
            "[2]Test Database Connection",
            "[Q]Exit"
        ]).ask()

#Define main function
def main():
    showGreeting()
    newLineBk()
    mainMenuOptions()

#Start main function
main()
