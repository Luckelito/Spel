import Variables
import Functions
from Classes import *
from math import *


class Coordinate:
    def __init__(self, true_name, name, health, x, y, is_cover, is_open, is_los, is_in_range, is_walkable, required_stamina, path, character, areas):
        self.true_name = true_name
        self.name = name
        self.health = health
        self.x = x
        self.y = y
        self.is_cover = is_cover
        self.is_open = is_open
        self.is_los = is_los
        self.is_in_range = is_in_range
        self.is_walkable = is_walkable
        self.required_stamina = required_stamina
        self.path = path
        self.character = character
        self.areas = areas

    def los(self, character_origin):
        if self.y - character_origin.y != 0:
            delta_y = (self.y - character_origin.y) / abs(self.y - character_origin.y)
        if self.x - character_origin.x != 0:
            delta_x = (self.x - character_origin.x) / abs(self.x - character_origin.x)

        if self.x - character_origin.x == 0 and self.y - character_origin.y == 0:
            return

        if self.x - character_origin.x == 0:
            for i in range(int(character_origin.y - self.y) + 1):
                if (self.y - delta_y * i) != character_origin.y:
                    if Variables.board[int(self.y - delta_y * i)][int(self.x)].is_cover:
                        return
            self.is_los = True
        elif self.y - character_origin.y == 0:
            for i in range(int(character_origin.x - self.x) + 1):
                if (self.x - delta_x * i) != character_origin.x:
                    if Variables.board[int(self.y - i)][int(self.x - delta_x * i)].is_cover:
                        return
            self.is_los = True

        elif abs((self.y - character_origin.y) / (self.x - character_origin.x)) < 1:
            for i in range(int((int(character_origin.x - self.x) ** 2 + int(character_origin.y - self.y) ** 2) ** 0.5)):
                if (self.x - delta_x * i) != character_origin.x or int(self.y - delta_y * round(abs((self.y - character_origin.y) / (self.x - character_origin.x)) * i)) != character_origin.y:
                    if Variables.board[int(self.y - delta_y * ceil(abs((self.y - character_origin.y) / (self.x - character_origin.x)) * i))][int(self.x - delta_x * i)].is_cover:
                        return
                    if Variables.board[int(self.y - delta_y * floor(abs((self.y - character_origin.y) / (self.x - character_origin.x)) * i))][int(self.x - delta_x * i)].is_cover:
                        return
            self.is_los = True
        elif abs((self.y - character_origin.y) / (self.x - character_origin.x)) >= 1:
            for i in range(int((int(character_origin.y - self.y) ** 2 + int(character_origin.x - self.x) ** 2) ** 0.5)):
                if int(self.y - delta_y * i) != character_origin.y or int(self.x - delta_x * round(abs((self.x - character_origin.x) / (self.y - character_origin.y)) * i)) != character_origin.x:
                    if Variables.board[int(self.y - delta_y * i)][int(self.x - delta_x * ceil(abs((self.x - character_origin.x) / (self.y - character_origin.y)) * i))].is_cover:
                        return
                    if Variables.board[int(self.y - delta_y * i)][int(self.x - delta_x * floor(abs((self.x - character_origin.x) / (self.y - character_origin.y)) * i))].is_cover:
                        return
            self.is_los = True
