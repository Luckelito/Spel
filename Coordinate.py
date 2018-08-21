import Variables
import Functions
from Classes import *

class Coordinate:
    def __init__(self, true_name, name, health, x, y, is_cover, is_open, is_los, is_walkable, is_shootable, required_stamina, path, character, areas):
        self.true_name = true_name
        self.name = name
        self.health = health
        self.x = x
        self.y = y
        self.is_cover = is_cover
        self.is_open = is_open
        self.is_los = is_los
        self.is_walkable = is_walkable
        self.is_shootable = is_shootable
        self.required_stamina = required_stamina
        self.path = path
        self.character = character
        self.areas = areas

    def los(self, character_origin):
        if self.x - character_origin.x > 0 and self.y - character_origin.y > 0:
            Functions.los_check(self, character_origin, 1, 1)
        elif self.x - character_origin.x < 0 and self.y - character_origin.y < 0:
            Functions.los_check(self, character_origin, -1, -1)
        elif self.x - character_origin.x > 0 and self.y - character_origin.y < 0:
            Functions.los_check(self, character_origin, 1, -1)
        elif self.x - character_origin.x < 0 and self.y - character_origin.y > 0:
            Functions.los_check(self, character_origin, -1, 1)
        elif self.x - character_origin.x == 0 and self.y - character_origin.y > 0:
            for i in range(int((int(character_origin.y - self.y) ** 2 + int(character_origin.x - self.x) ** 2) ** 0.5) + 1):
                if (self.y - i) != character_origin.y or (self.x - (self.x - character_origin.x) / (self.y - character_origin.y) * i) != \
                        character_origin.x:
                    if Variables.board[int(self.y - i)][int(self.x)].is_cover:
                        return
            self.is_los = True
        elif self.x - character_origin.x == 0 and self.y - character_origin.y < 0:
            for i in range(int((int(character_origin.y - self.y) ** 2 + int(character_origin.x - self.x) ** 2) ** 0.5) + 1):
                if (self.y + i) != character_origin.y or (self.x + (self.x - character_origin.x) / (self.y - character_origin.y) * i) != \
                        character_origin.x:
                    if Variables.board[int(self.y + i)][int(self.x)].is_cover:
                        return
            self.is_los = True
        elif self.y - character_origin.y == 0 and self.x - character_origin.x > 0:
            for i in range(int((int(character_origin.y - self.y) ** 2 + int(character_origin.x - self.x) ** 2) ** 0.5) + 1):
                if (self.x - i) != character_origin.x:
                    if Variables.board[int(self.y)][int(self.x - i)].is_cover:
                        return
            self.is_los = True
        elif self.y - character_origin.y == 0 and self.x - character_origin.x < 0:
            for i in range(int((int(character_origin.y - self.y) ** 2 + int(character_origin.x - self.x) ** 2) ** 0.5) + 1):
                if (self.x + i) != character_origin.x:
                    if Variables.board[int(self.y)][int(self.x + i)].is_cover:
                        return
            self.is_los = True
