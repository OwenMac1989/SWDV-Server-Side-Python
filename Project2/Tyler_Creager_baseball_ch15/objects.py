#!/usr/bin/env python3

import string


class Player:
    def __init__(self, name, position, bats, hits):
        self.name = name
        self.position = position
        self.bats = bats
        self.hits = hits
        self.batting_average = bats / hits


    def __str__(self):
        return f"{self.name} ({self.position}) - # Bats: {self.bats}\n# Hits: {self.hits}\nBatting Average: {self.batting_average}\n"
    
class Lineup:
    players: dict
    inputU: str
    def __init__(self):
        self.players = dict()
    def __iter__(self):
        for player in self.players:
            yield player
    def removePlayer(self, player: Player):
        if player in self.players:
            inputU = input(f"Are you sure you want to edit {player.name}? (y/n)").lower()
            if  inputU == "y":
                del self.players[player]
            else:
                print("Player not removed")
        else:
            print("Player not found in lineup")

    def addPlayer(self, player: Player):
        self.players[player.name] = player
        print(f"Player {player.name} added to lineup")

    def editPlayer(self, player: Player):
        if player in self.players:
            inputU = input(f"Are you sure you want to edit {player.name}? (y/n)").lower()
            if  inputU == "y":
                self.players[player.name] = player
            else:
                print("Player not edited")
        else:
            print("Player not found in lineup")