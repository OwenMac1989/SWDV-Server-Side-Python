#!/usr/bin/env python3
from ast import While
from asyncio.windows_events import NULL
import csv
import dis
from operator import contains
import sys
from datetime import date
from unittest import result
from xmlrpc.client import DateTime

FILENAME = "players.csv"

def exit_program():
    print("Terminating program.")
    sys.exit()
    
# Already using dictionary to store players. No need to change.
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
    
def getDate(today):
    date = input("When is Game Day? (MM-DD-YYYY) or input unknown: ").lower()
    if date == "unknown":
        return date
    if len(date) != 10:
        print("Invalid date format. Please enter a date in the format (MM-DD-YYYY)")
        getDate(today)
    if date[2] != "-" or date[5] != "-":
        print("Invalid date format. Please enter a date in the format (MM-DD-YYYY)")
        getDate(today)
    if contains(date[0:len(date)], "abcdefghijklmnopqrstuvwxyz"):
        print("Invalid date format. Please enter a date in the format (MM-DD-YYYY)")
        getDate(today)
    if int(date[6:10]) < int(today[6:10]) or int(date[3:5]) < int(today[3:5]) or int(date[0:2]) < int(today[0:2]):
        print("Game cannot be in the Past. Please enter a future date. (MM-DD-YYYY)")
        getDate(today)
    return date

def TodaysDate():
    today = date.today()
    today = today.strftime("%m-%d-%Y")
    return today

def daysTillGame(today, gameDate):
    today = today.split("-")
    gameDate = gameDate.split("-")
    result = f"Days until game: {int(gameDate[0]) * 30 + int(gameDate[1]) - int(today[0]) * 30 - int(today[1])}"
    return result

def displayDate():
    today = TodaysDate()
    gameDate = getDate(today)
    if gameDate == "unknown":
        print("Game date is unknown.")
        return
    result = daysTillGame(today, gameDate)
    if result == "":
        print("Please enter a valid date.")
        displayDate()
    else:
        print(f"Curent Date: {today}")
        print(f"Game Date: {gameDate}")
        print(result)


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