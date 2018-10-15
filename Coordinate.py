import Variables
import Functions
from Classes import *
from math import *


class Coordinate:
    def __init__(self, x, y):
        self.health = 0
        self.x = x
        self.y = y
        self.graphic_x_start = 0
        self.graphic_x_end = 0
        self.graphic_y_start = 0
        self.graphic_y_end = 0
        self.is_cover = False
        self.is_capture_point = False
        self.is_los = False
        self.is_in_range = False
        self.is_target = False
        self.required_stamina = 0
        self.path = []
        self.character = None
        self.areas = []

    def los(self, character_origin):
        if self.y - character_origin.y != 0:
            delta_y = (self.y - character_origin.y) / abs(self.y - character_origin.y)
        if self.x - character_origin.x != 0:
            delta_x = (self.x - character_origin.x) / abs(self.x - character_origin.x)

        if self.x - character_origin.x == 0 and self.y - character_origin.y == 0:
            return

        if self.x - character_origin.x == 0:
            for i in range(1, abs(int(self.y - character_origin.y))):
                if (self.y - delta_y * i) != character_origin.y:
                    if Variables.board[int(self.y - delta_y * i)][int(self.x)].is_cover:
                        return
            self.is_los = True

        elif self.y - character_origin.y == 0:
            for i in range(1, abs(int(self.x - character_origin.x))):
                if (self.x - delta_x * i) != character_origin.x:
                    if Variables.board[int(self.y)][int(self.x - delta_x * i)].is_cover:
                        return
            self.is_los = True

        elif abs((self.y - character_origin.y) / (self.x - character_origin.x)) < 1:
            for i in range(1, int((int(self.x - character_origin.x) ** 2 + int(self.y - character_origin.y) ** 2) ** 0.5)):
                if (self.x + delta_x * i) != character_origin.x or int(self.y - delta_y * round(abs((self.y - character_origin.y) / (self.x - character_origin.x)) * i)) != character_origin.y:
                    if Variables.board[int(self.y - delta_y * ceil(abs((self.y - character_origin.y) / (self.x - character_origin.x)) * i))][int(self.x - delta_x * i)].is_cover:
                        return
                    if Variables.board[int(self.y - delta_y * floor(abs((self.y - character_origin.y) / (self.x - character_origin.x)) * i))][int(self.x - delta_x * i)].is_cover:
                        return
            self.is_los = True

        elif abs((self.y - character_origin.y) / (self.x - character_origin.x)) >= 1:
            for i in range(1, int((int(self.y - character_origin.y) ** 2 + int(self.x - character_origin.x) ** 2) ** 0.5)):
                if int(self.y + delta_y * i) != character_origin.y or int(self.x - delta_x * round(abs((self.x - character_origin.x) / (self.y - character_origin.y)) * i)) != character_origin.x:
                    if Variables.board[int(self.y - delta_y * i)][int(self.x - delta_x * ceil(abs((self.x - character_origin.x) / (self.y - character_origin.y)) * i))].is_cover:
                        return

                    if Variables.board[int(self.y - delta_y * i)][int(self.x - delta_x * floor(abs((self.x - character_origin.x) / (self.y - character_origin.y)) * i))].is_cover:
                        return

                    if abs((self.x - character_origin.x) / (self.y - character_origin.y)) == 1 and \
                            Variables.board[int(self.y - delta_y * i + delta_y)][int(self.x - delta_x * i)].is_cover and \
                            Variables.board[int(self.y - delta_y * i)][int(self.x - delta_x * i + delta_x)].is_cover:
                        return
            self.is_los = True