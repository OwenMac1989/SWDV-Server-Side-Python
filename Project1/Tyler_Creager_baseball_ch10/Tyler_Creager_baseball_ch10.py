#!/usr/bin/env python3

from turtle import position
from Tyler_Creager_file_ch10 import *
## UI
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
    
## Player Manipulation
# list[0] name, [1] position, [2] bats, [3] hits, [4] average
def battingAverage(bats: int, hits: int):
    average:float
    try:
        hitsF = float(hits)
        batsF = float(bats)
        average = hitsF / batsF
        roundedAvg = round(average, 3)
    except ZeroDivisionError:
        average = 0 
        roundedAvg = 0
        return roundedAvg
    except ValueError:
        print("Invalid input")
    return roundedAvg





def getPlayerInfo(positions:tuple, name:str, position:str):
    playerInfoValid = False
    while playerInfoValid != True:              ## Start Player Info Loop

        nameValid = False
        positionValid = False
        try:
            while nameValid != True:
                name = input("Player's name: ")
                if name == "" or name == " ":
                    print("Must provide a name")
                elif name.isdigit():
                    print("Name cannot contain numbers")
                else:
                    nameValid = True
        except ValueError:
            print("Invalid input please try again!")


        while positionValid != True:
            try:
                position = input("Player's Position: ").lower()
                if position == "" or position == " ":
                    print("Must provide a valid position")
                else:
                    for i in positions:
                        if i.lower() == position:
                            positionValid = True
                    if positionValid == False:
                        print("Unable to find position please try again")
                        continue
            except ValueError:
                print("Invalid input please try again!")

        if nameValid == True and positionValid == True:
            playerInfoValid = True
            playerInfo = (name, position)
            return playerInfo              ## End Player Info Loop 

def getPlayerStats(bats:int, hits:int):
    valid = False
    batsValid = False
    hitsValid = False
    while valid != True:                        ## Start Player stats Loop

        try:
            while batsValid != True:
                bats = int(input("Official number of at bats: "))
                if bats == "" or bats == " ":
                    print("Must enter a number.")
                elif bats < 0:
                    print("Must be a valid number 0 or greater")
                else:
                    batsValid = True
        except ValueError:
            print("Invalid input please try again!")

        try:
            while hitsValid != True:
                hits = int(input("Number of hits: "))
                if hits == "" or hits == " ":
                    print("Must enter a number.")
                elif hits < 0:
                    print("Must be a valid number 0 or greater")
                elif hits > bats:
                    print("Hits cannot be greater than Bats.")
                else:
                    hitsValid = True
        except ValueError:
            print("Invalid input please try again!")

        if batsValid == True and hitsValid == True:
            valid = True 
            playerStats = (bats, hits)
            return playerStats    
        else: 
            print("Unable to validate information please try again!")                   ## End Player stats Loop

   
# list[0] name, [1] position, [2] bats, [3] hits, [4] average
def getPlayer(positions:tuple):
    positions = positions
    name:str = ""
    position:str =""
    bats:int = 0
    hits:int = 0
    playerX = []
    
    playerInfo = getPlayerInfo(positions, name, position)
    playerStats = getPlayerStats(bats, hits)
    print("Console Logging:")
    print(bats,hits)

    (name, position) = playerInfo
    (bats, hits) = playerStats

    avg = battingAverage(bats, hits)
    batsStr = str(bats)
    hitsStr = str(hits)
    avgStr = str(avg)


    playerX.append(name)
    playerX.append(position)
    playerX.append(batsStr)
    playerX.append(hitsStr)
    playerX.append(avgStr)
    return playerX

def editPlayerInfo(players:dict, positions):
    editConfirm = False 
    while editConfirm != True:
        try:
            playerName = input("Enter the player name of the player being edited: ")
            if playerName == "" or playerName == " ":
                print("Name cannot be empty")
            elif playerName.isdigit():
                    print("Name cannot contain numbers")
            else:
                counter = 0
                for i in players:
                    player = players[i]
                    if player[0] == playerName:
                        counter = i
                        print("Found the Player")
                        break
            player = players[counter]
        except ValueError:
            print("Invalid input please try again!")

        if playerName == player[0]:
            print("editing player")
            name = ""
            position = ""
            (name, position) = getPlayerInfo(positions, name, position)
            player[0] = name
            player[1] = position
            players[counter] = player
            editConfirm = True
            return players
        else:
            print("Unable to find player please try again")

def editPlayerStats(players:dict):
    editConfirm = False 
    while editConfirm != True:
        try:
            playerName = input("Enter the player name of the player being edited: ")
            if playerName == "" or playerName == " ":
                print("Name cannot be empty")
            elif playerName.isdigit():
                    print("Name cannot contain numbers")
            else:
                counter = 0
                for i in players:
                    player = players[i]
                    if player[0] == playerName:
                        counter = i
                        print("Found the Player")
                        break
        except ValueError:
            print("Invalid input please try again!")
        player = players[counter]

        if playerName == player[0]:
            print("editing player")
            bats = 0
            hits = 0
            (bats, hits) = getPlayerStats(bats, hits)
            average = battingAverage(bats, hits)
            batsStr = str(bats)
            hitsStr = str(hits)
            averageStr = str(average)
            player[2] = batsStr
            player[3] = hitsStr
            player[4] = averageStr
            players[counter] = player
            editConfirm = True
            return players
        else:
            print("Unable to find player please try again")

def deletePlayer(players:dict):
    deleteConfirm = False 
    while deleteConfirm != True:
        try:
            playerName = input("Enter the player name of the player being removed")
            if playerName == "" or playerName == " ":
                print("Name cannot be empty")
            elif playerName.isdigit():
                    print("Name cannot contain numbers")
            else:
                counter = 0
                for i in players:
                    player = players[i]
                    if player[0] == playerName:
                        counter = i
                        print("Found the Player")
                        break
        except ValueError:
            print("Invalid input please try again!")

        player = players[counter]
        if playerName == player[0]:
            print("deleting player")
            players.pop(counter)
            deleteConfirm = True
            return players
def defineTable():
    player = "Player's name:"
    position = "Player Position:"
    bats = "Official number of at bats:"
    hits = "Number of hits:"
    avg = "Batting average:"
    sep ="-"
    for i in range(125):
        print(sep, end='')
    print()        
    print(f"{player:<20}{position:<20}{bats:<30}{hits:<20}{avg:<20}")

# list[0] name, [1] position, [2] bats, [3] hits, [4] average
def displayPlayer(playerX:list ):

    name = playerX[0]
    position = playerX[1]
    bats = playerX[2]
    hits = playerX[3]
    avg = playerX[4]
    readPlayer = f"{name:<20}{position:<20}{bats:<30}{hits:<20}{avg:<20}"
    print()
    print(readPlayer)


## Player Manipulation End

def main():
    intro()
    menu()





if __name__ == "__main__":
    main()
    