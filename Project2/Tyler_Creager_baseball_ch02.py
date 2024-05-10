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


def main():
    intro()
    player1 = getPlayer()
    player1 = battingAverage(player1)
    displayPlayer(player1)




if __name__ == "__main__":
    main()