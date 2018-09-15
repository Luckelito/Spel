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

    def walk_movement(self, destination, requires_stamina, can_jump):  # requires_stamina and can_jump = BOOL
        if can_jump:
            if type(destination.character) == Character:
                if requires_stamina:
                    moves = destination.required_stamina
                    self.move += moves
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
                        Functions.boardstate()

                Functions.reset_board()
                Functions.target(destination, 2)
                for row in Variables.board:
                    for place in row:
                        if place.is_in_range:
                            place.name = (str(place.x) + "," + str(place.y))

                Functions.boardstate()

                action = input("Choose where to jump (x,y):")
                while True:
                    if Variables.board[int(action[-1])][int(action[0])].is_in_range and type(Variables.board[int(action[-1])][int(action[0])].character) != Character:
                        self.jump_movement(Variables.board[int(action[-1])][int(action[0])])
                        self.move = self.speed
                        Functions.reset_board()
                        return moves
                    else:
                        action = input("Choose a valid location (x,y):")

        print("Destination:" + str(destination.x) + ", " + str(destination.y))

        for place in destination.path:
            print(place.x, place.y)

        if requires_stamina:
            moves = destination.required_stamina
            self.move += moves
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
                Functions.boardstate()

        return moves

    def jump_movement(self, destination):
        if len(destination.areas) > 0:
            for area in destination.areas:
                if area.character.team != self.team:
                    Functions.deal_damage(area.character, self, area.area_damage)
        Functions.placement_swap(self, destination)
        Functions.reset_board()
        Functions.boardstate()
