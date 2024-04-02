#!/usr/bin/env python3
from ast import While
from asyncio.windows_events import NULL
import csv
import sys

FILENAME = "players.csv"

def exit_program():
    print("Terminating program.")
    sys.exit()

def readPlayers():
    players:dict = dict()
    player: list = []
    try:
        player = []
        with open(FILENAME,"r", newline="") as file:
            reader = csv.reader(file)
            counter = 0
            for row in reader:
                players[counter] = row
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


def writePlayers(players):
    try:
        with open(FILENAME, "w", newline="") as file:
            writer = csv.writer(file)
            for i in players:
                writer.writerow(players[i])
               

    except OSError as e:
        print(type(e), e)
        exit_program()
    except Exception as e:
        print(type(e), e)
        exit_program()