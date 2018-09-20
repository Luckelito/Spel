import Variables
import Functions
import Classes


class CircleWeapon:
    def __init__(self, hit_damage=20, area_damage=40, weapon_range=3, stamina_cost=3, character=None, areas=[]):
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

        action = input("Confirm attack (yes=y,no=n):")
        while True:
            if action == "y":
                for row in Variables.board:
                    for place in row:
                        if place.y - self.character.coordinate.y != 0:
                            delta_y = (place.y - self.character.coordinate.y) / abs(place.y - self.character.coordinate.y)
                        if place.x - self.character.coordinate.x != 0:
                            delta_x = (place.x - self.character.coordinate.x) / abs(place.x - self.character.coordinate.x)

                        if place.y - self.character.coordinate.y == 0 and place.x - self.character.coordinate.x == 0:
                            break

                        if place.x - self.character.coordinate.x == 0:
                            for i in range(1, (place.y - self.character.coordinate.y) + 1):
                                if 0 < self.character.coordinate.y + delta_y * i < Variables.board_width:
                                    if Variables.board[int(self.character.coordinate.y + delta_y * i)][self.character.coordinate.x].is_los:
                                        Variables.board[int(self.character.coordinate.y + delta_y * i)][self.character.coordinate.x].is_in_range = True
                                    elif Variables.board[int(self.character.coordinate.y + delta_y * i)][self.character.coordinate.x].is_cover:
                                        Functions.damage_cover(Variables.board[int(self.character.coordinate.y + delta_y * i)][self.character.coordinate.x], 1)
                                    else:
                                        break

                        elif place.y - self.character.coordinate.y == 0:
                            for i in range(1, (place.x - self.character.coordinate.x) + 1):
                                if 0 < self.character.coordinate.x + delta_x * i < Variables.board_width:
                                    if Variables.board[self.character.coordinate.y][int(self.character.coordinate.x + delta_x * i)].is_los:
                                        Variables.board[self.character.coordinate.y][int(self.character.coordinate.x + delta_x * i)].is_in_range = True
                                    elif Variables.board[self.character.coordinate.y][int(self.character.coordinate.x + delta_x * i)].is_cover:
                                        Functions.damage_cover(Variables.board[self.character.coordinate.y][int(self.character.coordinate.x + delta_x * i)], 1)
                                    else:
                                        break

                        elif abs((place.y - self.character.coordinate.y) / (place.x - self.character.coordinate.x)) <= 1:
                            for i in range(1, (place.x - self.character.coordinate.x) + 1):
                                if 0 <= self.character.coordinate.x + delta_x * i < Variables.board_width and 0 <= int(self.character.coordinate.y + delta_y * round(abs((place.y - self.character.coordinate.y) / (place.x - self.character.coordinate.x)) * i)) < Variables.board_height:
                                    if Variables.board[int(self.character.coordinate.y + delta_y * round(abs((place.y - self.character.coordinate.y) / (place.x - self.character.coordinate.x)) * i))][int(self.character.coordinate.x + delta_x * i)].is_los:
                                        Variables.board[int(self.character.coordinate.y + delta_y * round(abs((place.y - self.character.coordinate.y) / (place.x - self.character.coordinate.x)) * i))][int(self.character.coordinate.x + delta_x * i)].is_in_range = True
                                    elif Variables.board[int(self.character.coordinate.y + delta_y * round(abs((place.y - self.character.coordinate.y) / (place.x - self.character.coordinate.x)) * i))][int(self.character.coordinate.x + delta_x * i)].is_cover:
                                        Functions.damage_cover(Variables.board[int(self.character.coordinate.y + delta_y * round(abs((place.y - self.character.coordinate.y) / (place.x - self.character.coordinate.x)) * i))][int(self.character.coordinate.x + delta_x * i)], 1)
                                    else:
                                        break

                        elif abs((place.y - self.character.coordinate.y) / (place.x - self.character.coordinate.x)) > 1:
                            for i in range(1, (place.y - self.character.coordinate.y) + 1):
                                if 0 <= self.character.coordinate.y + delta_y * i < Variables.board_height and 0 <= self.character.coordinate.x + delta_x * round(abs((place.x - self.character.coordinate.x) / (place.y - self.character.coordinate.y)) * i) < Variables.board_width:
                                    if Variables.board[int(self.character.coordinate.y + delta_y * i)][int(self.character.coordinate.x + delta_x * round(abs((place.x - self.character.coordinate.x) / (place.y - self.character.coordinate.y)) * i))].is_los:Variables.board[int(self.character.coordinate.y + delta_y * i)][int(self.character.coordinate.x + delta_x * round(abs((place.x - self.character.coordinate.x) / (place.y - self.character.coordinate.y)) * i))].is_in_range = True
                                    elif Variables.board[int(self.character.coordinate.y + delta_y * i)][int(self.character.coordinate.x + delta_x * round(abs((place.x - self.character.coordinate.x) / (place.y - self.character.coordinate.y)) * i))].is_cover:
                                        Functions.damage_cover(Variables.board[int(self.character.coordinate.y + delta_y * i)][int(self.character.coordinate.x + delta_x * round(abs((place.x - self.character.coordinate.x) / (place.y - self.character.coordinate.y)) * i))], 1)
                                    else:
                                        break

                for row in Variables.board:
                    for place in row:
                        if place.is_in_range:
                            self.apply_area(place)

                self.character.has_shot = True
                self.character.has_shield = False

                Functions.reset_board()
                Functions.boardstate()

                return self.stamina_cost

            elif action == "n":
                return 0

            else:
                action = input("Confirm attack (yes=y,no=n):")

    def apply_area(self, place):
        place.areas.append(self)
        if type(place.character) == Classes.Character:
            if place.character.team == self.character.team:
                Functions.deal_damage(self.character, place.character, self.hit_damage, True)

