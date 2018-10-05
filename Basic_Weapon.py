import Variables
import Functions
import Classes
import pygame
from math import *


class BasicWeapon:
    def __init__(self, hit_damage=50, area_damage=30, weapon_range=6, stamina_cost=3, character=None, areas=[]):
        self.hit_damage = hit_damage
        self.area_damage = area_damage
        self.weapon_range = weapon_range
        self.stamina_cost = stamina_cost
        self.character = character
        self.areas = areas

    def shoot(self):
        Functions.target_los(self.character.coordinate, self.weapon_range)
        pressed_key = pygame.key.get_pressed()
        pressed_mouse = pygame.mouse.get_pressed()
        mouse_pos = pygame.mouse.get_pos()

        for row in Variables.board:
            for place in row:
                if place.graphic_x_start <= mouse_pos[0] < place.graphic_x_end and place.graphic_y_start <= mouse_pos[1] < place.graphic_y_end:
                    if place.y - self.character.coordinate.y != 0:
                        delta_y = (place.y - self.character.coordinate.y) / abs(place.y - self.character.coordinate.y)
                    if place.x - self.character.coordinate.x != 0:
                        delta_x = (place.x - self.character.coordinate.x) / abs(place.x - self.character.coordinate.x)

                    if place.y - self.character.coordinate.y == 0 and place.x - self.character.coordinate.x == 0:
                        return 0

                    if place.x - self.character.coordinate.x == 0:
                        for i in range(1, self.weapon_range + 1):
                            if 0 < self.character.coordinate.y + delta_y * i < Variables.board_width:
                                if Variables.board[int(self.character.coordinate.y + delta_y * i)][self.character.coordinate.x].is_los:
                                    Variables.board[int(self.character.coordinate.y + delta_y * i)][self.character.coordinate.x].is_in_range = True
                                elif Variables.board[int(self.character.coordinate.y + delta_y * i)][self.character.coordinate.x].is_cover:
                                    Functions.damage_cover(Variables.board[int(self.character.coordinate.y + delta_y * i)][self.character.coordinate.x], 1)
                                else:
                                    break

                    elif place.y - self.character.coordinate.y == 0:
                        for i in range(1, self.weapon_range + 1):
                            if 0 < self.character.coordinate.x + delta_x * i < Variables.board_width:
                                if Variables.board[self.character.coordinate.y][int(self.character.coordinate.x + delta_x * i)].is_los:
                                    Variables.board[self.character.coordinate.y][int(self.character.coordinate.x + delta_x * i)].is_in_range = True
                                elif Variables.board[self.character.coordinate.y][int(self.character.coordinate.x + delta_x * i)].is_cover:
                                    Functions.damage_cover(Variables.board[self.character.coordinate.y][int(self.character.coordinate.x + delta_x * i)], 1)
                                else:
                                    break

                    elif abs((place.y - self.character.coordinate.y) / (place.x - self.character.coordinate.x)) <= 1:
                        for i in range(1, self.weapon_range + 1):
                            if 0 <= self.character.coordinate.x + delta_x * i < Variables.board_width and 0 <= int(self.character.coordinate.y + delta_y * round(abs((place.y - self.character.coordinate.y) / (place.x - self.character.coordinate.x)) * i)) < Variables.board_height:
                                if Variables.board[int(self.character.coordinate.y + delta_y * round(abs((place.y - self.character.coordinate.y) / (place.x - self.character.coordinate.x)) * i))][int(self.character.coordinate.x + delta_x * i)].is_los:
                                    Variables.board[int(self.character.coordinate.y + delta_y * round(abs((place.y - self.character.coordinate.y) / (place.x - self.character.coordinate.x)) * i))][int(self.character.coordinate.x + delta_x * i)].is_in_range = True
                                elif Variables.board[int(self.character.coordinate.y + delta_y * round(abs((place.y - self.character.coordinate.y) / (place.x - self.character.coordinate.x)) * i))][int(self.character.coordinate.x + delta_x * i)].is_cover:
                                    Functions.damage_cover(Variables.board[int(self.character.coordinate.y + delta_y * round(abs((place.y - self.character.coordinate.y) / (place.x - self.character.coordinate.x)) * i))][int(self.character.coordinate.x + delta_x * i)], 1)
                                else:
                                    break

                    elif abs((place.y - self.character.coordinate.y) / (place.x - self.character.coordinate.x)) > 1:
                        for i in range(1, self.weapon_range + 1):
                            if 0 <= self.character.coordinate.y + delta_y * i < Variables.board_height and 0 <= self.character.coordinate.x + delta_x * round(abs((place.x - self.character.coordinate.x) / (place.y - self.character.coordinate.y)) * i) < Variables.board_width:
                                if Variables.board[int(self.character.coordinate.y + delta_y * i)][int(self.character.coordinate.x + delta_x * round(abs((place.x - self.character.coordinate.x) / (place.y - self.character.coordinate.y)) * i))].is_los:
                                    Variables.board[int(self.character.coordinate.y + delta_y * i)][int(self.character.coordinate.x + delta_x * round(abs((place.x - self.character.coordinate.x) / (place.y - self.character.coordinate.y)) * i))].is_in_range = True
                                elif Variables.board[int(self.character.coordinate.y + delta_y * i)][int(self.character.coordinate.x + delta_x * round(abs((place.x - self.character.coordinate.x) / (place.y - self.character.coordinate.y)) * i))].is_cover:
                                    Functions.damage_cover(Variables.board[int(self.character.coordinate.y + delta_y * i)][int(self.character.coordinate.x + delta_x * round(abs((place.x - self.character.coordinate.x) / (place.y - self.character.coordinate.y)) * i))], 1)
                                else:
                                    break

                    for row in Variables.board:
                        for place in row:
                            if place.is_in_range:
                                self.apply_area(place)
                                self.areas.append(place)

                    self.character.has_shot = True
                    self.character.has_shield = False

                    Functions.reset_board()

                    self.character.is_shooting = False

                    return self.stamina_cost

        return 0


    def apply_area(self, place):
        place.areas.append(self)
        if type(place.character) == Classes.Character:
            if place.character.team == self.character.team:
                Functions.deal_damage(self.character, place.character, self.hit_damage, True)
