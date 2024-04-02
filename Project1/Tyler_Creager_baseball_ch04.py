#!/usr/bin/env python3

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

# list[0] name, [1] bats, [2] hits
def getPlayer():
    playerX = []
    name = input("Player's name: ")
    bats = input("Official number of at bats: ")
    hits = input("Number of hits: ")
    playerX.append(name)
    playerX.append(bats)
    playerX.append(hits)
    return playerX

# list[3] average
def battingAverage(playerX:list):
    bats = int(playerX[1])
    hits = int(playerX[2])
    average = float(hits / bats)
    roundedAvg = round(average, 3)
    playerX.append(roundedAvg)
    return playerX

def displayPlayer(playerX:list ):
    name = playerX[0]
    bats = playerX[1]
    hits = playerX[2]
    avg = playerX[3]
    readPlayer = f"Player's name: {name}\nOfficial number of at bats: {bats}\nNumber of hits: {hits}\nBatting average: {avg}"
    # print(readPlayer)
    print(f"{name}'s batting average is {avg}")


def menu():
    players = dict()
    menuOptions = f"MENU OPTIONS:\nCalc- Calculate a batting average.\nExit- exit program.\nHelp- display instructions."
    print(menuOptions)
    cont = True
    while cont == True:
        numPlayers = 0
        print()
        userInput = input("Command: ")
        print()
        if userInput.lower() == "calc":
            numPlayers += 1
            players[numPlayers] = getPlayer()
            players[numPlayers] = battingAverage(players[numPlayers])
            displayPlayer(players[numPlayers])
            print()
            divider()
        elif userInput.lower() == "exit":
            print("Exiting! Thank you for your patronage")
            divider()
            cont = False
        elif userInput.lower() == "help":
            print(menuOptions)
            divider()
        else:
            print("Unknown input please try again")
        

def main():
    intro()





if __name__ == "__main__":
    main()
    menu()