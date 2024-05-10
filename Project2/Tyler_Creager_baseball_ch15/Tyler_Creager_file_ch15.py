#!/usr/bin/env python3
from ast import While
from asyncio.windows_events import NULL
import csv
import sys
from objects import *


FILENAME = "players15.csv"

def exit_program():
    print("Terminating program.")
    sys.exit()

def readPlayers(players:dict):
    lineup = Lineup()
    lineup.players = players
    try:
        with open(FILENAME,"r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                row = str(row)
                row = row.replace('"', '')
                row = row.replace('[', '')
                row = row.replace(']', '')
                row = row.replace('\'', '')
                row = row.split(",")
                playerX = Player(row[0], row[1], int(row[2]), int(row[3]))
                lineup.addPlayer(playerX)
        return lineup.players
    except FileNotFoundError:
        print("File could not be found!!!")
        with open(FILENAME, "w", newline="") as file:
            print("Creating File")
        return lineup
    except Exception as e:
        print(type(e), e)
        exit_program()
    
def writePlayers(players:dict):
    lineup = Lineup()
    lineup.players = players
    try:
        with open(FILENAME, "w", newline="") as file:
            writer = csv.writer(file)
            for player in lineup.players:
                list = []
                playerx = lineup.players[player]
                string = f"{playerx.name},{playerx.position},{str(playerx.bats)},{str(playerx.hits)}"
                print(string)
                list.append(string)
                writer.writerow(list)
               

    except OSError as e:
        print(type(e), e)
        exit_program()
    except Exception as e:
        print(type(e), e)
        exit_program()