from Classes import *
import Functions
import Variables

class Character:
    def __init__(self, true_name, name, speed, health, team, move, shoot, coordinate, weapon, has_shield):
        self.true_name = true_name
        self.name = name
        self.speed = speed
        self.health = health
        self.team = team
        self.move = move
        self.shoot = shoot
        self.coordinate = coordinate
        self.weapon = weapon
        self.has_shield = has_shield

    def __repr__(self):
        return self.name

    def walk_movement(self, destination, requires_stamina): #requires_stamina = BOOL
        for place in Variables.board[int(destination[-1])][int(destination[0])].path:
            if len(place.areas) > 0:
                for area in place.areas:
                    if area.character.team != self.team:
                        Functions.deal_damage(area.character, self.character, area.area_damage)
            Functions.placement_swap(self, place)
            Functions.reset_board()
            Functions.boardstate()

        Functions.placement_swap(self, Variables.board[int(destination[-1])][int(destination[0])])

        if requires_stamina:
            moves = Variables.board[int(destination[-1])][int(destination[0])].required_stamina
            self.move += moves
        else:
            moves = 0

        Functions.reset_board()
        Functions.boardstate()

        print(moves)
        return moves

    def jump_movement(self, destination):
        if len(destination.areas) > 0:
            for area in destination.areas:
                if area.character.team != self.team:
                    Functions.deal_damage(area.character, self, area.area_damage)
        Functions.placement_swap(self, destination)
        Functions.reset_board()
        Functions.boardstate()
