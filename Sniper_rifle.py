import Variables
import Functions
import Classes


class SniperRifle:
    def __init__(self, hit_damage=70, area_damage=0, weapon_range=10, stamina_cost=3, character=None, areas=[]):
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
                if type(Variables.board[int(action.split(",")[-1])][int(action.split(",")[0])].character) == Classes.Character:
                    Functions.deal_damage(self.character, Variables.board[int(action.split(",")[-1])][int(action.split(",")[0])].character, self.hit_damage, False)

                    Functions.reset_board()
                    Functions.boardstate()

                    self.character.has_shot = True
                    self.character.has_shield = False

                    return self.stamina_cost
                else:
                    action = input("Choose where you want to shoot ((x,y) or c=cancel):")

