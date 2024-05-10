#!/usr/bin/env python3
from getdate import *
from mainUI import *
from data import *
from objects import *
from Tyler_Creager_file_ch15 import *
def intro():

    title = "Baseball Team Manager"
    presentTitle = title.center(60)
    summary = "This program calculates the batting average for a player based" "\n on the player's official number of at bats and hits."
    
    divider()
    print(presentTitle)
    print()
    print(f"{summary:^30}")
    print()
    divider()
    redo = 'y'
    while redo == 'y':
        displayDate()
        redo = input("Would you like to change the date? (y/n): ").lower()
    divider()


def divider():
    sep = "="
    for i in range (100):
        print(sep, end='')
    print()

def menu():
    lineup: Lineup = Lineup()
    positions: tuple = ("C", "1B", "2B", "3B", "SS", "LF", "CF", "RF", "P")
    placeholder:str = ""
    players = lineup.players
    lineup.players = readPlayers(players)
    menuOptions = f"MENU OPTIONS:\nDisp - Display LineUp.\nAdd - Add Player.\nRemove - Remove Player.\nMove - Move Player.\nEdit - Edit Player Position\n" \
    "Edit Stat - Edit Player Stats\nHelp - Display Commands\nExit - Exit Program"
    print(menuOptions)
    for i in positions:
        if i == "P":
            placeholder += i
        else:
            placeholder += i
            placeholder += ", "
    print(f"\nPositions: {placeholder}")
    cont = True

    while cont == True:
        print()
        userInput = input("Command: ")
        print()

        if userInput.lower() == "disp":
            defineTable()
            displayPlayer(lineup)
            print()
            divider()

        elif userInput.lower() == "add":
            lineup.addPlayer(getPlayer(positions))
            displayPlayer(lineup)
            print()
            divider()
        
        elif userInput.lower() == "edit":
            editPlayerInfo(lineup, positions)
            print()
            divider()

        elif userInput.lower() == "edit stat":
            editPlayerStats(lineup)
            print()
            divider()
        
            
        elif userInput.lower() == "exit":
            players = lineup.players
            print("Saving to file")
            writePlayers(players)
            print("Exiting! Thank you for your patronage")
            exit_program()
            divider()
            cont = False

        elif userInput.lower() == "help":
            print(menuOptions)
            divider()

        else:
            print("Unknown input please try again")

## End UI