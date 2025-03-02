import sys
import os
from datetime import datetime

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

appInializationDate = datetime.now()
currentPath = os.getcwd()
processID = os.getpid()
pythonVersion = sys.version
gitHubLink = "https://github.com/leventeberry/pySQL"
author = "LeVente Berry Jr."

fullGreet = f"{greeting} \n Created By: {author} \n App Started at: {appInializationDate} \n App Process ID: {processID} \n App Path: {currentPath} \n GitHub Link: {gitHubLink}"


def showGreeting():
    return fullGreet
