from Classes import *
import Functions
import Variables
import pygame


class Character:
    def __init__(self, name=None, speed=4, health=10, team=None, weapon=None, character_jump_range=3, character_jump_damage=10):
        self.name = name
        self.speed = speed
        self.health = health
        self.team = team
        self.has_moved = False
        self.has_shot = False
        self.has_rushed = False
        self.coordinate = None
        self.weapon = weapon
        self.has_shield = True
        self.character_jump_range = character_jump_range
        self.character_jump_damage = character_jump_damage
        self.is_shooting = False
        self.is_rushing = False
        self.is_jumping = False

    def __repr__(self):
        return self.name

    def walk_movement(self, destination, requires_stamina, can_jump):  # requires_stamina and can_jump = BOOL
        if can_jump:
            if type(destination.character) == Character:
                for place in destination.path:
                    if len(place.areas) > 0:
                        for area in place.areas:
                            if area.character.team != self.team:
                                Functions.deal_damage(area.character, self, area.area_damage, True)
                    if type(place.character) != Character:
                        Functions.placement_swap(self, place)
                        Functions.reset_board()

                Functions.reset_board()
                Functions.target(destination, 3)

                pressed_key = pygame.key.get_pressed()
                pressed_mouse = pygame.mouse.get_pressed()
                mouse_pos = pygame.mouse.get_pos()

                for row in Variables.board:
                    for place in row:
                        if place.graphic_x_start <= mouse_pos[0] < place.graphic_x_end and place.graphic_y_start <= mouse_pos[1] < place.graphic_y_end:
                            if Variables.board[int(place.y)][int(place.x)].is_in_range:
                                moves = destination.required_stamina
                                if place.character == self:
                                    self.has_moved = self.speed
                                    return moves
                                elif type(place.character) == Character:
                                    return 0
                                elif pressed_key[pygame.K_ESCAPE]:
                                    return 0
                                else:
                                    self.jump_movement(Variables.board[int(place.y)][int(place.x)])
                                    self.has_moved = self.speed
                                    Functions.reset_board()
                                    return moves

        if requires_stamina:
            moves = destination.required_stamina
            self.has_moved += moves
        else:
            moves = 0

        for place in destination.path:
            if len(place.areas) > 0:
                for area in place.areas:
                    if area.character.team != self.team:
                        Functions.deal_damage(area.character, self, area.area_damage, True)
            if type(place.character) != Character:
                Functions.placement_swap(self, place)
                Functions.reset_board()

        return moves

    def jump_movement(self, destination):
        if len(destination.areas) > 0:
            for area in destination.areas:
                if area.character.team != self.team:
                    Functions.deal_damage(area.character, self, area.area_damage, True)
        Functions.placement_swap(self, destination)
        Functions.reset_board()
