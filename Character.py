from Classes import *

class Character:
    def __init__(self, true_name, name, speed, health, team, move, shoot, coordinate):
        self.true_name = true_name
        self.name = name
        self.speed = speed
        self.health = health
        self.team = team
        self.move = move
        self.shoot = shoot
        self.coordinate = coordinate

    def __repr__(self):
        return self.name