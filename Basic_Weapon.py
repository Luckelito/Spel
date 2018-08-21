import Variables
import Functions
import Classes
from math import *


class BasicWeapon:
    def __init__(self, hit_damage=50, area_damage=30, weapon_range=4, stamina_cost=3, character=None):
        self.hit_damage = hit_damage
        self.area_damage = area_damage
        self.weapon_range = weapon_range
        self.stamina_cost = stamina_cost
        self.character = character

    def shoot(self):
        Functions.target_los(self.character.coordinate, self.weapon_range)

        for row in Variables.board:
            for place in row:
                if place.is_los:
                    if type(place.character) == Classes.Character:
                        place.character.name = (place.character.true_name + " " + str(place.x) + "," + str(place.y))
                    else:
                        place.name = (str(place.x) + "," + str(place.y) + "(" + str(place.required_stamina) + ")")

        Functions.boardstate()

        action = input("Choose where you want to shoot ((x,y) or c=cancel):")
        while True:
            if "," in action:
                while True:
                    target = Variables.board[action[1]][action[0]]
                    delta_y = (target.y - self.character.coordinate.y) / abs(target.y - self.character.coordinate.y)
                    delta_x = (target.x - self.character.coordinate.x) / abs(target.x - self.character.coordinate.x)
                    if abs((target.y - self.character.coordinate.y) / (target.x - self.character.coordinate.x)) < 1:
                        for i in range(self.weapon_range):
                            if (target.x - delta_x * i) != self.character.coordinate.x or int(target.y - delta_y * round(abs((target.y - self.character.coordinate.y) / (target.x - self.character.coordinate.x)) * i)) != self.character.coordinate.y:
                                if Variables.board[int(target.y - delta_y * round(abs((target.y - self.character.coordinate.y) / (target.x - self.character.coordinate.x)) * i))][int(target.x - delta_x * i)].is_cover:
                                    return
                    elif abs((place.y - self.character.coordinate.y) / (place.x - self.character.coordinate.x)) >= 1:
                        for i in range(int((int(self.character.coordinate.y - place.y) ** 2 + int(self.character.coordinate.x - place.x) ** 2) ** 0.5)):
                            if int(place.y - delta_y * i) != self.character.coordinate.y or int(place.x - delta_x * round(abs((place.x - self.character.coordinate.x) / (place.y - self.character.coordinate.y)) * i)) != self.character.coordinate.x:
                                if Variables.board[int(place.y - delta_y * i)][int(place.x - delta_x * ceil(abs((place.x - self.character.coordinate.x) / (place.y - self.character.coordinate.y)) * i))].is_cover:
                                    return
                                if Variables.board[int(place.y - delta_y * i)][int(place.x - delta_x * floor(abs((place.x - self.character.coordinate.x) / (place.y - self.character.coordinate.y)) * i))].is_cover:
                                    return
                        place.is_los = True

                        for row in Variables.board:
                            for place in row:
                                if place.is_shootable:
                                    print(place.x+","+place.y)
                                    place.name = "."

                        Functions.boardstate()
                        Functions.reset_board()

                        return self.stamina_cost
                    break
            elif action == "c":
                return 0
            else:
                Functions.boardstate()
                action = input("Choose a valid target ((x,y) or c=cancel):")