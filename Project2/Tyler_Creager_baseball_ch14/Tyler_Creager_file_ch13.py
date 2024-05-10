#!/usr/bin/env python3
from ast import While
from asyncio.windows_events import NULL
import csv
import sys
from player import Player


FILENAME = "players.csv"

def exit_program():
    print("Terminating program.")
    sys.exit()

def readPlayers():
    players:dict = dict()

    try:
        player = []
        with open(FILENAME,"r", newline="") as file:
            reader = csv.reader(file)
            counter = 0
            for row in reader:
                playerX = Player(row[0], row[1], int(row[2]), int(row[3]))
                players[counter] = playerX
                counter += 1
        return players
    except FileNotFoundError:
        print("File could not be found!!!")
        with open(FILENAME, "w", newline="") as file:
            print("Creating File")
        return players
    except Exception as e:
        print(type(e), e)
        exit_program()
    
def writePlayers(players:dict):
    try:
        with open(FILENAME, "w", newline="") as file:
            writer = csv.writer(file)
            for i in players:
                string = players[i].name + "," + players[i].position + "," + str(players[i].bats) + "," + str(players[i].hits)
                writer.writerow(string)
               

    except OSError as e:
        print(type(e), e)
        exit_program()
    except Exception as e:
        print(type(e), e)
        exit_program()