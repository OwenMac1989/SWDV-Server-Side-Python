#!/usr/bin/env python3
from objects import *

## Player Manipulation
# list[0] name, [1] position, [2] bats, [3] hits, [4] average

# def battingAverage(bats: int, hits: int):
#     average:float
#     try:
#         hitsF = float(hits)
#         batsF = float(bats)
#         average = hitsF / batsF
#         roundedAvg = round(average, 3)
#     except ZeroDivisionError:
#         average = 0 
#         roundedAvg = 0
#         return roundedAvg
#     except ValueError:
#         print("Invalid input")
#     return roundedAvg

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

    
    playerInfo = getPlayerInfo(positions, name, position)
    playerStats = getPlayerStats(bats, hits)
    print("Console Logging:")
    print(bats,hits)

    (name, position) = playerInfo
    (bats, hits) = playerStats

    playerX = Player(name, position, bats, hits)

    return playerX

def editPlayerInfo(lineup:Lineup, positions):
    editConfirm = False 
    while editConfirm != True:
        try:
            playerName = input("Enter the player name of the player being edited: ")
            if playerName == "" or playerName == " ":
                print("Name cannot be empty")
            elif playerName.isdigit():
                    print("Name cannot contain numbers")
            else:
                playerx = lineup.players[playerName]
                print("editing player")
                name = ""
                position = ""
                (name, position) = getPlayerInfo(positions, name, position)
                playerx.name = name
                playerx.position = position                
                lineup.editPlayer(playerx)
                editConfirm = True
        except ValueError:
            print("Invalid input please try again!")
    return lineup

def editPlayerStats(lineup:Lineup):
    editConfirm = False 
    while editConfirm != True:
        try:
            playerName = input("Enter the player name of the player being edited: ")
            if playerName == "" or playerName == " ":
                print("Name cannot be empty")
            elif playerName.isdigit():
                    print("Name cannot contain numbers")
            else:
                playerx = lineup.players[playerName]
                print("editing player")
                bats = 0
                hits = 0
                (bats, hits) = getPlayerStats(bats, hits)
                playerx.bats = bats
                playerx.hits = hits
                playerx.average = bats / hits
                lineup.editPlayer(playerx)
                editConfirm = True
        except ValueError:
           print("Invalid input please try again!")
    return lineup

def deletePlayer(lineup:Lineup):
    editConfirm = False 
    while editConfirm != True:
        try:
            playerName = input("Enter the player name of the player being edited: ")
            if playerName == "" or playerName == " ":
                print("Name cannot be empty")
            elif playerName.isdigit():
                    print("Name cannot contain numbers")
            else:
                playerx = lineup.players[playerName]
                lineup.removePlayer(playerx)
                editConfirm = True
        except ValueError:
           print("Invalid input please try again!")
    return lineup
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
def displayPlayer(lineup: Lineup):
    print(lineup.players)
    for player in lineup.players:
        playerx = lineup.players[player]
        readPlayer = f"{playerx.name:<20}{playerx.position:<20}{playerx.bats:<30}{playerx.hits:<20}{playerx.batting_average:<20}"
        print()
        print(readPlayer)


## Player Manipulation End