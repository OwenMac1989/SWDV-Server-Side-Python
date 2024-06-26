#!/usr/bin/env python3

from Tyler_Creager_file_ch07 import *
## UI
def intro():

    title = "Baseball Team Manager"
    presentTitle = title.center(60)
    summary = "This program calculates the batting average for a player\n based"\
    " on the player's official number of at bats and hits."
    divider()
    print(presentTitle)
    print(f"\n {summary}")
    divider()


def divider():
    sep = "="
    for i in range (60):
        print(sep, end='')
    print()

def menu():

    positions: tuple = ("C", "1B", "2B", "3B", "SS", "LF", "CF", "RF", "P")
    players = readPlayers()
    menuOptions = f"MENU OPTIONS:\nDisp- Display LineUp.\nAdd- Add Player.\nRemove- Remove Player.\nMove- Move Player.\nEdit- Edit Player Position\n" \
    "Edit Stat- Edit Player Stats\nHelp- Display Commands\nExit- Exit Program"
    print(menuOptions)
    cont = True

    while cont == True:
        numberOfPlayers = 0 
        for i in players:
            numberOfPlayers += 1
        print()
        userInput = input("Command: ")
        print()


        if userInput.lower() == "disp":
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
    average = float(hits / bats)
    roundedAvg = round(average, 3)
    return roundedAvg

def getPlayerInfo(positions:tuple, name:str, position:str):
    playerInfoValid = False
    while playerInfoValid != True:              ## Start Player Info Loop

        nameValid = False
        positionValid = False
        
        while nameValid != True:
            name = input("Player's name: ")
            if name == "" or name == " ":
                print("Must provide a name")
            elif name.isdigit():
                print("Name cannot contain numbers")
            else:
                nameValid = True

        while positionValid != True:
            position = input("Player's Position: ")
            if position == "" or position == " ":
                print("Must provide a valid position")
            else:
                for i in positions:
                    if i.lower() == position:
                        positionValid = True
                if positionValid == False:
                    print("Unable to find position please try again")
                    continue

        if nameValid == True and positionValid == True:
            playerInfoValid = True
            playerInfo = (name, position)
            return playerInfo              ## End Player Info Loop 

def getPlayerStats(bats:int, hits:int):
    valid = False
    batsValid = False
    hitsValid = False
    while valid != True:                        ## Start Player stats Loop

        while batsValid != True:
            bats = int(input("Official number of at bats: "))
            if bats == "" or bats == " ":
                print("Must enter a number.")
            elif bats < 0:
                print("Must be a valid number 0 or greater")
            else:
                batsValid = True

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
        player = players[counter]
        if playerName == player[0]:
            print("deleting player")
            players.pop(counter)
            deleteConfirm = True
            return players


# list[0] name, [1] position, [2] bats, [3] hits, [4] average
def displayPlayer(playerX:list ):

    name = playerX[0]
    position = playerX[1]
    bats = playerX[2]
    hits = playerX[3]
    avg = playerX[4]
    readPlayer = f"Player's name: {name}\nPlayer Position: {position}\nOfficial number of at bats: {bats}\nNumber of hits: {hits}\nBatting average: {avg}"
    print(readPlayer)


## Player Manipulation End

def main():
    intro()
    menu()





if __name__ == "__main__":
    main()
    