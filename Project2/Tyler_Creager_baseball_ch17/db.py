#!/usr/bin/env python3
from datetime import date
from operator import contains
from asyncio.windows_events import NULL
import csv
import sys
from turtle import position
from objects import *
import sqlite3
from contextlib import closing


## Convert DB Methods for Baseball Manager to SQLite
#-#-#-#-#-##-#-#-#-#-##-#-#-#-#-##-#-#-#-#-##-#-#-#-#-##-#-#-#-#-##-#-#-#-#-##-#-#-#-#-##-#-#-#-#-##-#-#-#-#-##-#-#-#-#-##-#-#-#-#-#
conn = None

def connect():
    global conn
    if not conn:
        DB_FILE = "__BaseBallDB/BaseBallDB.sqlite"
        conn = sqlite3.connect(DB_FILE)
        conn.row_factory = sqlite3.Row

def close():
    if conn:
        conn.close()

def make_player(row):
    return Player(row["firstName"], row["lastName"], row["batOrder"], row["position"], row["atBats"], row["hits"])

def make_position(row):
    return Position(row["positionID"], row["positionSymbol"], row["positionName"])

def get_players():
    query = '''SELECT playerID, CONCAT(firstName + lastNam) as Name, batOrder, position, atBats, hits
               FROM Player'''
    with closing(conn.cursor()) as c:
        c.execute(query)
        results = c.fetchall()
    players = []
    for row in results:
        players.append(make_player(row))
    return players

def get_positions():
    query = '''SELECT positionID, positionSymbol as position, positionName as Name
               FROM Position'''
    with closing(conn.cursor()) as c:
        c.execute(query)
        results = c.fetchall()
    positions = []
    for row in results:
        positions.append(make_position(row))
    return positions

def get_position(positionID):
    query = '''SELECT categoryID, name AS categoryName
               FROM Category WHERE categoryID = ?'''
    with closing(conn.cursor()) as c:
        c.execute(query, (positionID,))
        row = c.fetchone()
        if row:
            return make_position(row)
        else:
            return None
## Reference for future methods
# def get_movies_by_category(category_id):
#     query = '''SELECT movieID, Movie.name, year, minutes,
#                       Movie.categoryID as categoryID,
#                       Category.name as categoryName
#                FROM Movie JOIN Category
#                       ON Movie.categoryID = Category.categoryID
#                WHERE Movie.categoryID = ?'''
#     with closing(conn.cursor()) as c:
#         c.execute(query, (category_id,))
#         results = c.fetchall()

#     movies = []
#     for row in results:
#         movies.append(make_movie(row))
#     return movies

# def get_movies_by_year(year):
#     query = '''SELECT movieID, Movie.name, year, minutes,
#                       Movie.categoryID as categoryID,
#                       Category.name as categoryName
#                FROM Movie JOIN Category
#                       ON Movie.categoryID = Category.categoryID
#                WHERE year = ?'''
#     with closing(conn.cursor()) as c:
#         c.execute(query, (year,))
#         results = c.fetchall()

#     movies = []
#     for row in results:
#         movies.append(make_movie(row))
#     return movies

# def get_movies_by_minutes(minutes):
#     query = '''SELECT movieID, Movie.name, year, minutes,
#                       Movie.categoryID as categoryID,
#                       Category.name as categoryName
#                FROM Movie JOIN Category
#                       ON Movie.categoryID = Category.categoryID
#                WHERE minutes <= ? 
#                ORDER BY minutes ASC'''
#     with closing(conn.cursor()) as c:
#         c.execute(query, (minutes,))
#         results = c.fetchall()

#     movies = []
#     for row in results:
#         movies.append(make_movie(row))
#     return movies

# def get_movie(movie_id):
#     query = '''SELECT movieID, Movie.name, year, minutes, Movie.categoryID
#                 FROM Movie
#                 WHERE movieID = ?'''
#     with closing(conn.cursor()) as c:
#         c.execute(query, (movie_id,))
#         results = c.fetchall()
#         movie = []
#         for row in results:
#             movie.append(make_movie(row))
#         return movie

# def add_movie(movie):
#     sql = '''INSERT INTO Movie (categoryID, name, year, minutes) 
#              VALUES (?, ?, ?, ?)'''
#     with closing(conn.cursor()) as c:
#         c.execute(sql, (movie.category.id, movie.name, movie.year,
#                         movie.minutes))
#         conn.commit()

# def delete_movie(movie_id):
#     sql = '''DELETE FROM Movie WHERE movieID = ?'''
#     with closing(conn.cursor()) as c:
#         c.execute(sql, (movie_id,))
#         test = conn.commit()
#         print("Test", test)

## Get Data
#-#-#-#-#-##-#-#-#-#-##-#-#-#-#-##-#-#-#-#-##-#-#-#-#-##-#-#-#-#-##-#-#-#-#-##-#-#-#-#-##-#-#-#-#-##-#-#-#-#-##-#-#-#-#-##-#-#-#-#-#
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
## End Get Data
#-#-#-#-#-##-#-#-#-#-##-#-#-#-#-##-#-#-#-#-##-#-#-#-#-##-#-#-#-#-##-#-#-#-#-##-#-#-#-#-##-#-#-#-#-##-#-#-#-#-##-#-#-#-#-##-#-#-#-#-#

## Player Manipulation
# list[0] name, [1] position, [2] bats, [3] hits, [4] average
#-#-#-#-#-##-#-#-#-#-##-#-#-#-#-##-#-#-#-#-##-#-#-#-#-##-#-#-#-#-##-#-#-#-#-##-#-#-#-#-##-#-#-#-#-##-#-#-#-#-##-#-#-#-#-##-#-#-#-#-#
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
            player.name = name
            player.position = position
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
            player.bats = bats
            player.hits = hits
            player.average = bats / hits
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
def displayPlayer(playerX:Player ):
    readPlayer = f"{playerX.name:<20}{playerX.position:<20}{playerX.bats:<30}{playerX.hits:<20}{playerX.batting_average:<20}"
    print()
    print(readPlayer)


## Player Manipulation End
#-#-#-#-#-##-#-#-#-#-##-#-#-#-#-##-#-#-#-#-##-#-#-#-#-##-#-#-#-#-##-#-#-#-#-##-#-#-#-#-##-#-#-#-#-##-#-#-#-#-##-#-#-#-#-##-#-#-#-#-#

## Date Manipulation
#-#-#-#-#-##-#-#-#-#-##-#-#-#-#-##-#-#-#-#-##-#-#-#-#-##-#-#-#-#-##-#-#-#-#-##-#-#-#-#-##-#-#-#-#-##-#-#-#-#-##-#-#-#-#-##-#-#-#-#-#

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
#-#-#-#-#-##-#-#-#-#-##-#-#-#-#-##-#-#-#-#-##-#-#-#-#-##-#-#-#-#-##-#-#-#-#-##-#-#-#-#-##-#-#-#-#-##-#-#-#-#-##-#-#-#-#-##-#-#-#-#-#