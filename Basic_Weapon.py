import Variables
import Functions
import Classes
import pygame
from math import *


class BasicWeapon:
    def __init__(self, hit_damage=50, area_damage=30, weapon_range=6, stamina_cost=3, character=None):
        self.hit_damage = hit_damage
        self.area_damage = area_damage
        self.weapon_range = weapon_range
        self.stamina_cost = stamina_cost
        self.character = character
        self.areas = []

    def shoot(self):
        Functions.reset_board(True, True)
        Functions.target_los(self.character.coordinate, self.weapon_range)

        pressed_key = pygame.key.get_pressed()
        pressed_mouse = pygame.mouse.get_pressed()
        mouse_pos = pygame.mouse.get_pos()

        if pressed_key[pygame.K_ESCAPE]:
            self.character.is_shooting = False
            return 0

        for row in Variables.board:
            for place in row:
                if place.graphic_x_start <= mouse_pos[0] < place.graphic_x_end and place.graphic_y_start <= mouse_pos[1] < place.graphic_y_end:
                    if place == self.character.coordinate:
                        return 0
                    else:
                        Functions.straight_line(self.character.coordinate, place, self.weapon_range)

        if pressed_mouse[0]:
            for row in Variables.board:
                for place in row:
                    if place.is_in_range:
                        if not place.is_cover:
                            self.apply_area(place)
                        else:
                            Functions.damage_cover(place, 1)

            self.character.has_shot = True
            self.character.has_shield = False

            Functions.reset_board(True, True)

            self.character.is_shooting = False

            return self.stamina_cost

        else:
            for row in Variables.board:
                for place in row:
                    if place.is_in_range:
                        place.is_target = True
                    elif place.is_los:
                        place.is_in_range = True

        return 0

    def apply_area(self, place):
        place.areas.append(self)
        if type(place.character) == Classes.Character:
            if place.character.team != self.character.team:
                Functions.deal_damage(self.character, place.character, self.hit_damage, True)
        self.areas.append(place)
