from initialize import showGreeting as greeting
from rich.console import Console

console = Console()
bkpoint = "\n////////////////////////////////////////////////////////////////////////////\n"

#Create Line Break Function
def newLineBk():
    console.print(f"[green]{bkpoint}[/green]")

#Define main function
def main():
    greeting()
    newLineBk()

#Start main function
main()
