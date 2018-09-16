import Variables
import Functions
import Classes
from math import *


class BasicWeapon:
    def __init__(self, hit_damage=50, area_damage=30, weapon_range=4, stamina_cost=3, character=None, areas=[]):
        self.hit_damage = hit_damage
        self.area_damage = area_damage
        self.weapon_range = weapon_range
        self.stamina_cost = stamina_cost
        self.character = character
        self.areas = areas

    def shoot(self):
        Functions.target_los(self.character.coordinate, self.weapon_range)

        for row in Variables.board:
            for place in row:
                if place.is_los:
                    if type(place.character) == Classes.Character:
                        place.character.name = (place.character.true_name + " " + str(place.x) + "," + str(place.y))
                    else:
                        place.name = (str(place.x) + "," + str(place.y))

        Functions.boardstate()

        action = input("Choose where you want to shoot ((x,y) or c=cancel):")
        while True:
            if "," in action:
                while True:
                    target = Variables.board[int(action.split(",")[-1])][int(action.split(",")[0])]
                    if target.y - self.character.coordinate.y != 0:
                        delta_y = (target.y - self.character.coordinate.y) / abs(target.y - self.character.coordinate.y)
                    if target.x - self.character.coordinate.x != 0:
                        delta_x = (target.x - self.character.coordinate.x) / abs(target.x - self.character.coordinate.x)

                    if target.y - self.character.coordinate.y == 0 and target.x - self.character.coordinate.x == 0:
                        return

                    if target.x - self.character.coordinate.x == 0:
                        for i in range(1, self.weapon_range + 1):
                            if 0 < self.character.coordinate.y + delta_y * i < Variables.board_width:
                                if Variables.board[int(self.character.coordinate.y + delta_y * i)][self.character.coordinate.x].is_los:
                                    Variables.board[int(self.character.coordinate.y + delta_y * i)][self.character.coordinate.x].is_in_range = True
                                elif Variables.board[int(self.character.coordinate.y + delta_y * i)][self.character.coordinate.x].is_cover:
                                    Functions.damage_cover(Variables.board[int(self.character.coordinate.y + delta_y * i)][self.character.coordinate.x], 1)
                                else:
                                    break

                    elif target.y - self.character.coordinate.y == 0:
                        for i in range(1, self.weapon_range + 1):
                            if 0 < self.character.coordinate.x + delta_x * i < Variables.board_width:
                                if Variables.board[self.character.coordinate.y][int(self.character.coordinate.x + delta_x * i)].is_los:
                                    Variables.board[self.character.coordinate.y][int(self.character.coordinate.x + delta_x * i)].is_in_range = True
                                elif Variables.board[self.character.coordinate.y][int(self.character.coordinate.x + delta_x * i)].is_cover:
                                    Functions.damage_cover(Variables.board[self.character.coordinate.y][int(self.character.coordinate.x + delta_x * i)], 1)
                                else:
                                    break

                    elif abs((target.y - self.character.coordinate.y) / (target.x - self.character.coordinate.x)) <= 1:
                        for i in range(1, self.weapon_range + 1):
                            if 0 < self.character.coordinate.x + delta_x * i < Variables.board_width and 0 < int(self.character.coordinate.y + delta_y * round(abs((target.y - self.character.coordinate.y) / (target.x - self.character.coordinate.x)) * i)) < Variables.board_height:
                                if Variables.board[int(self.character.coordinate.y + delta_y * round(abs((target.y - self.character.coordinate.y) / (target.x - self.character.coordinate.x)) * i))][int(self.character.coordinate.x + delta_x * i)].is_los:
                                    Variables.board[int(self.character.coordinate.y + delta_y * round(abs((target.y - self.character.coordinate.y) / (target.x - self.character.coordinate.x)) * i))][int(self.character.coordinate.x + delta_x * i)].is_in_range = True
                                elif Variables.board[int(self.character.coordinate.y + delta_y * round(abs((target.y - self.character.coordinate.y) / (target.x - self.character.coordinate.x)) * i))][int(self.character.coordinate.x + delta_x * i)].is_cover:
                                    Functions.damage_cover(Variables.board[int(self.character.coordinate.y + delta_y * round(abs((target.y - self.character.coordinate.y) / (target.x - self.character.coordinate.x)) * i))][int(self.character.coordinate.x + delta_x * i)], 1)
                                else:
                                    break

                    elif abs((target.y - self.character.coordinate.y) / (target.x - self.character.coordinate.x)) > 1:
                        for i in range(1, self.weapon_range + 1):
                            if 0 < self.character.coordinate.y + delta_y * i < Variables.board_height and 0 < self.character.coordinate.x + delta_x * round(abs((target.x - self.character.coordinate.x) / (target.y - self.character.coordinate.y)) * i) < Variables.board_width:
                                if Variables.board[int(self.character.coordinate.y + delta_y * i)][int(self.character.coordinate.x + delta_x * round(abs((target.x - self.character.coordinate.x) / (target.y - self.character.coordinate.y)) * i))].is_los:
                                    Variables.board[int(self.character.coordinate.y + delta_y * i)][int(self.character.coordinate.x + delta_x * round(abs((target.x - self.character.coordinate.x) / (target.y - self.character.coordinate.y)) * i))].is_in_range = True
                                elif Variables.board[int(self.character.coordinate.y + delta_y * i)][int(self.character.coordinate.x + delta_x * round(abs((target.x - self.character.coordinate.x) / (target.y - self.character.coordinate.y)) * i))].is_cover:
                                    Functions.damage_cover(Variables.board[int(self.character.coordinate.y + delta_y * i)][int(self.character.coordinate.x + delta_x * round(abs((target.x - self.character.coordinate.x) / (target.y - self.character.coordinate.y)) * i))], 1)
                                else:
                                    break

                    for row in Variables.board:
                        for place in row:
                            if place.is_in_range:
                                self.apply_area(place)
                                self.areas.append(place)

                    Functions.reset_board()
                    Functions.boardstate()

                    self.character.has_shot = True
                    self.has_shield = False

                    return self.stamina_cost
            elif action == "c":
                Functions.reset_board()
                return 0
            else:
                Functions.boardstate()
                action = input("Choose a valid target ((x,y) or c=cancel):")

    def apply_area(self, place):
        place.areas.append(self)
        if type(place.character) == Classes.Character:
            Functions.deal_damage(self.character, place.character, self.hit_damage)
