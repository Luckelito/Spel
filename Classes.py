class Character:
    name = "A"
    speed = 3
    health = 100
    team = 1
    move = 0
    shoot = 0
    weapon_1 = 0
    weapon_2 = 1

    def __repr__(self):
        return self.name

    def info(self):
        print("Health: " + self.health + '/n' + "Speed: " + self.speed)

    def __init__(self, name, speed = 3, health = 200, team = 1, move = 0, shoot = 0, weapon_1 = 0, weapon_2 = 0):
        self.name = name
        self.speed = speed
        self.health = health
        self.team = team
        self.move = move
        self.shoot = shoot
        self.weapon_1 = weapon_1
        self.weapon_2 = weapon_2

class Weapon:
    def __repr__(self):
        return self.name

    def __init__(self,name,damage=0,range_=0,dropoff=0,area_of_effect=0):
        self.name = name
        self.damage = damage
        self.range_ = range_
        self.dropoff = dropoff
        self.area_of_effect = area_of_effect

class Open_ground:
    name = "_"

    def _repr_(self):
        return self.name

    def __init__(self, name="_"):
        self.name = name

class Cover:
    name = 5

    def _repr_(self):
        return self.name

    def __init__(self, name):
        self.name = name

#class Board:
#    Height = 10
#    Width = 10
#    Standard_board = 0
#
#    def __init__(self, health = 5):
#        self.health = health