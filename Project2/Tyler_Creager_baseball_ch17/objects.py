#!/usr/bin/env python3

class Player:
    def __init__(self, name, position, bats, hits):
        self.name = name
        self.position = position
        self.bats = bats
        self.hits = hits
        self.batting_average = bats / hits


    def __str__(self):
        return f"{self.name} ({self.position}) - # Bats: {self.bats}\n# Hits: {self.hits}\nBatting Average: {self.batting_average}\n"