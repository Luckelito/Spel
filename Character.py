from Classes import *
import Functions
import Variables
import pygame


class Character:
    def __init__(self, name=None, speed=4, health=100, team=None, weapon=None, character_jump_range=3, character_jump_damage=10):
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
        self.is_moving = False
        self.current_destination = []

    def __repr__(self):
        return self.name

    def walk_movement(self, destination, requires_stamina, can_jump):  # requires_stamina and can_jump = BOOL
        self.is_moving = True

        if len(self.current_destination) == 0:
            self.current_destination = destination.path

        if self.is_jumping:
            Functions.reset_board()
            Functions.target(self.current_destination[-1], 3)

            pressed_key = pygame.key.get_pressed()
            pressed_mouse = pygame.mouse.get_pressed()
            mouse_pos = pygame.mouse.get_pos()

            if pressed_key[pygame.K_ESCAPE]:
                self.is_jumping = False
                return 0

            if pressed_mouse[0]:
                for row in Variables.board:
                    for place in row:
                        if place.graphic_x_start <= mouse_pos[0] < place.graphic_x_end and place.graphic_y_start <= \
                                mouse_pos[1] < place.graphic_y_end:
                            if Variables.board[int(place.y)][int(place.x)].is_in_range:
                                if type(place.character) == Character:
                                    return 0
                                elif place.character == self:
                                    self.current_destination.append(place)
                                else:
                                    self.current_destination.append(place)

            current_time = pygame.time.get_ticks()
            if Variables.passed_time - current_time >= 1000:
                Variables.passed_time = pygame.time.get_ticks()

                if len(self.current_destination) == 1:
                    self.jump_movement(self.current_destination[0])
                    self.has_moved = self.speed
                    self.is_moving = False
                    return self.current_destination[0].required_stamina

                else:
                    if len(self.current_destination[0].areas) > 0:
                        for area in self.current_destination[0].areas:
                            if area.character.team != self.team:
                                Functions.deal_damage(area.character, self, area.area_damage, True)

                    if type(self.current_destination[0].character) != Character:
                        Functions.placement_swap(self, self.current_destination[0])
                        Functions.reset_board()

                    self.current_destination.remove(self.current_destination[0])

            return 0

        if can_jump:
            if type(self.current_destination[-1].character) == Character:
                self.is_jumping = True
                return 0

        if requires_stamina:
            moves = self.current_destination[-1].required_stamina
            self.has_moved += moves
        else:
            moves = 0

        current_time = pygame.time.get_ticks()
        if current_time - Variables.passed_time >= 1000:
            Variables.passed_time = pygame.time.get_ticks()

            if len(self.current_destination) == 1:
                Functions.placement_swap(self, self.current_destination[0])
                Functions.reset_board()
                self.has_moved = self.speed
                self.is_moving = False
                return self.current_destination[0].required_stamina

            else:
                if len(self.current_destination[0].areas) > 0:
                    for area in self.current_destination[0].areas:
                        if area.character.team != self.team:
                            Functions.deal_damage(area.character, self, area.area_damage, True)
                if type(self.current_destination[0].character) != Character:
                    Functions.placement_swap(self, self.current_destination[0])
                    Functions.reset_board()

                self.current_destination.remove(self.current_destination[0])

        return moves

    def jump_movement(self, destination):
        if len(destination.areas) > 0:
            for area in destination.areas:
                if area.character.team != self.team:
                    Functions.deal_damage(area.character, self, area.area_damage, True)
        Functions.placement_swap(self, destination)
        Functions.reset_board()
