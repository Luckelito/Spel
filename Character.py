from Classes import *
import Functions
import Variables

class Character:
    def __init__(self, true_name=None, name=None, speed=4, health=100, team=None, move=0, shoot=False, rushed=False, coordinate=None, weapon=None, has_shield=True, character_jump_range=3, character_jump_damage=10):
        self.true_name = true_name
        self.name = name
        self.speed = speed
        self.health = health
        self.team = team
        self.has_moved = move
        self.has_shot = shoot
        self.has_rushed = rushed
        self.coordinate = coordinate
        self.weapon = weapon
        self.has_shield = has_shield
        self.character_jump_range = character_jump_range
        self.character_jump_damage = character_jump_damage

    def __repr__(self):
        return self.name

    def walk_movement(self, destination, requires_stamina, can_jump):  # requires_stamina and can_jump = BOOL
        if can_jump:
            if type(destination.character) == Character:
                if requires_stamina:
                    moves = destination.required_stamina
                    self.has_moved += moves
                else:
                    moves = 0

                for place in destination.path:
                    if len(place.areas) > 0:
                        for area in place.areas:
                            if area.character.team != self.team:
                                Functions.deal_damage(area.character, self, area.area_damage)
                    if type(place.character) != Character:
                        Functions.placement_swap(self, place)
                        Functions.reset_board()

                Functions.reset_board()
                Functions.target(destination, 3)
                for row in Variables.board:
                    for place in row:
                        if place.is_in_range:
                            place.name = (str(place.x) + "," + str(place.y))

                action = input("Choose where to jump (x,y):")
                while True:
                    if "," in action:
                        if Variables.board[int(action.split(",")[-1])][int(action.split(",")[0])].is_in_range:
                            if type(Variables.board[int(action.split(",")[-1])][int(action.split(",")[0])].character) == Character:
                                if Variables.board[int(action.split(",")[-1])][int(action.split(",")[0])].character == self:
                                    self.jump_movement(Variables.board[int(action.split(",")[-1])][int(action.split(",")[0])])
                                    self.has_moved = self.speed
                                    return moves
                                else:
                                    action = input("Choose a valid location (x,y):")
                            else:
                                self.jump_movement(Variables.board[int(action[-1])][int(action[0])])
                                self.has_moved = self.speed
                                Functions.reset_board()
                                return moves
                        else:
                            action = input("Choose a valid location (x,y):")
                    else:
                        action = input("Choose a valid location (x,y):")

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
