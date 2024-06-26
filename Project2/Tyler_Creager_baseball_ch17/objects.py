#!/usr/bin/env python3
class Position:
    def __init__(self, positionID, positionSymbol, positionName):
        self.positionID = positionID
        self.positionSymbol = positionSymbol
        self.positionName = positionName

    def __str__(self):
        return f"{self.positionID} {self.positionName} - ({self.positionSymbol})"
class Player:
    def __init__(self, firstName, lastName, battingOrder, position, bats, hits):
        self.firstName = firstName
        self.lastName = lastName
        self.battingOrder = battingOrder
        self.position = position
        self.bats = bats
        self.hits = hits
        self.batting_average = bats / hits


    def __str__(self):
        return f"{self.firstName} {self.lastName} (#Order {self.battingOrder} Pos: {self.position}) - # Bats: {self.bats}\n# Hits: {self.hits}\nBatting Average: {self.batting_average}\n"