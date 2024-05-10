#!/usr/bin/env python3
from db import *
from mainUI import *
from objects import *
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

    positions: tuple = ("C", "1B", "2B", "3B", "SS", "LF", "CF", "RF", "P")
    placeholder:str = ""
    players = readPlayers()
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
        numberOfPlayers = 0 
        for i in players:
            numberOfPlayers += 1
        print()
        userInput = input("Command: ")
        print()


        if userInput.lower() == "disp":
            defineTable()
            for playerX in players:
                displayPlayer(players[playerX])
                print()
            print()
            divider()

        elif userInput.lower() == "add":
            players[numberOfPlayers] = getPlayer(positions)
            displayPlayer(players[numberOfPlayers])
            numberOfPlayers += 1
            print()
            divider()
        
        elif userInput.lower() == "edit":
            editPlayerInfo(players, positions)
            print()
            divider()

        elif userInput.lower() == "edit stat":
            editPlayerStats(players)
            print()
            divider()
        
            
        elif userInput.lower() == "exit":
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