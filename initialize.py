import sys
import os
from datetime import datetime

from rich.console import Console

console = Console()

greeting = r"""
////////////////////////////////////////////////////////////////////////////
//                                                                        //
//    _______           _______  _______  _           __       _______    //
//   (  ____ )|\     /|(  ____ \(  ___  )( \         /  \     (  __   )   //
//   | (    )|( \   / )| (    \/| (   ) || (         \/) )    | (  )  |   //
//   | (____)| \ (_) / | (_____ | |   | || |           | |    | | /   |   //
//   |  _____)  \   /  (_____  )| |   | || |           | |    | (/ /) |   //
//   | (         ) (         ) || | /\| || |           | |    |   / | |   //
//   | )         | |   /\____) || (_\ \ || (____/\   __) (_ _ |  (__) |   //
//   |/          \_/   \_______)(____\/_)(_______/   \____/(_)(_______)   //
//                                                                        //
////////////////////////////////////////////////////////////////////////////
"""

appInitializationDate = datetime.now()
currentPath = os.getcwd()
processID = os.getpid()
pythonVersion = sys.version
gitHubLink = "https://github.com/leventeberry/pySQL"
author = "LeVente Berry Jr."
fullGreet = f"[green]{greeting}[/green] \n [yellow]Created By[/yellow]: {author} \n [yellow]App Started at[/yellow]: {appInitializationDate} \n [yellow]App Process ID[/yellow]: {processID} \n [yellow]App Path[/yellow]: {currentPath} \n [yellow]GitHub Link[/yellow]: {gitHubLink}"

def showGreeting():
    console.print(fullGreet)
