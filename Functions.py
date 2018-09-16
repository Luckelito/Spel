from math import *
from itertools import *
from random import *
import Variables
import Classes


def equip(character, weapon_class):
    character.weapon = weapon_class(character=character)


def starting_positions(board_height, board_width):
    placement_swap(Variables.A, Variables.board[int(board_height/2 + 1)][0])
    placement_swap(Variables.B, Variables.board[int(board_height/2)][0])
    placement_swap(Variables.C, Variables.board[int(board_height/2 - 1)][0])
    placement_swap(Variables.a, Variables.board[int(board_height/2 + 1)][int(board_width - 1)])
    placement_swap(Variables.b, Variables.board[int(board_height/2)][int(board_width - 1)])
    placement_swap(Variables.c, Variables.board[int(board_height/2 - 1)][int(board_width - 1)])


def boardstate():
    inverted_board = reversed(Variables.board)
    print("")
    for row in inverted_board:
        for place in row:
            if type(place.character) == Classes.Character:
                if place.character.has_shield:
                    print((" " * int(floor(4 - (len(place.character.name) / 2))) + "(" + place.character.name + ")" + ceil(3 - (len(place.character.name) / 2)) * " "), end="")
                else:
                    print((" " * int(floor(5 - (len(place.character.name) / 2))) + place.character.name + ceil(4 - (len(place.character.name) / 2)) * " "), end="")
            elif len(place.areas) > 0:
                print((" " * int(floor(5 - (len(place.areas) / 2))) + "." * len(place.areas) + ceil(4 - (len(place.areas) / 2)) * " "), end="")
            elif place.is_cover:
                print((" " * 4 + str(place.health) + 4 * " "), end="")
            elif "," in place.name:
                index = place.name.index(",")
                print(" " * (4 - index) + place.name + " " * (5 - (len(place.name) - index)), end="")
            else:
                print((" " * int(floor(5 - (len(place.name) / 2))) + place.name + ceil(4 - (len(place.name) / 2)) * " "), end="")
        print("\n")


def reset_board():
    for row in Variables.board:
        for place in row:
            place.is_los = False
            place.is_walkable = False
            place.is_in_range = False
            place.name = place.true_name
            if type(place.character) == Classes.Character:
                place.character.name = place.character.true_name


def placement_swap(character, destination):
    if type(character.coordinate) == Classes.Coordinate:
        character.coordinate.character = None
    character.coordinate = destination
    destination.character = character


def choose_character():
    reset_board()
    current_team = []
    for character in Variables.characters_alive:
        if character.team == Variables.players_turn:
            current_team.append(character)

    selected_character = input("Choose your character " + str(current_team) + ":")
    while True:
        k = 0
        for character in current_team:
            if str(character.name) == str(selected_character):
                return character
            else:
                k += 1
        if k == len(current_team):
            selected_character = input("Please choose a valid character " + str(current_team) + ":")


def target(origin, ability_range):
    for row in Variables.board:
        for place in row:
            if ((origin.x - place.x) ** 2 + (origin.y - place.y) ** 2) ** 0.5 <= ability_range:
                place.is_in_range = True


def target_los(origin, ability_range):
    for row in Variables.board:
        for place in row:
            if ((origin.x - place.x) ** 2 + (origin.y - place.y) ** 2) ** 0.5 <= ability_range:
                place.los(origin)


def target_walk(origin, ability_range):
    legal_targets = [[], [], []]

    for combination in (product("210", repeat=ability_range*2)):
        z = 0
        u = 0
        place = [0, 0]
        place[0] = origin.x
        place[1] = origin.y
        current_path = []
        while True:
            x = int(combination[z]) - 1
            y = int(combination[int(z+len(combination)/2)]) - 1

            if place[0] + x == origin.x and place[1] + y == origin.y:
                break

            elif x != 0 and y != 0:
                if u <= ability_range - 2 ** 0.5:
                    if 0 <= place[0] + x <= Variables.board_width - 1 and 0 <= place[1] + y <= Variables.board_height - 1:
                        if not Variables.board[place[1] + y][place[0] + x].is_cover:
                            if 0 <= place[0] + 2 * x <= Variables.board_width - 1 and 0 <= place[1] + 2 * y <= Variables.board_height - 1:
                                place[0] += x
                                place[1] += y
                                current_path.append(Variables.board[place[1]][place[0]])
                                u += 2 ** 0.5
                                Variables.board[place[1]][place[0]].is_walkable = True
                                if u < Variables.board[place[1]][place[0]].required_stamina:
                                    Variables.board[place[1]][place[0]].required_stamina = ceil(u)
                                    Variables.board[place[1]][place[0]].path = []
                                    for place_path in current_path:
                                        Variables.board[place[1]][place[0]].path.append(place_path)
                            else:
                                break
                        else:
                            break
                    else:
                        break
                else:
                    break
            elif x != 0 or y != 0:
                if 0 <= place[0] + x <= Variables.board_width - 1 and 0 <= place[1] + y <= Variables.board_height - 1:
                    if not Variables.board[place[1] + y][place[0] + x].is_cover:
                        place[0] += x
                        place[1] += y
                        current_path.append(Variables.board[place[1]][place[0]])
                        u += 1
                        Variables.board[place[1]][place[0]].is_walkable = True
                        if u < Variables.board[place[1]][place[0]].required_stamina:
                            Variables.board[place[1]][place[0]].required_stamina = ceil(u)
                            Variables.board[place[1]][place[0]].path = []
                            for place_path in current_path:
                                Variables.board[place[1]][place[0]].path.append(place_path)
                    else:
                        break
                else:
                    break
            else:
                break

            if u > ability_range - 1:
                break

            z += 1

    return legal_targets


def turn(character):
    reset_board()
    if character.speed - character.move > Variables.stamina:
        target_walk(character.coordinate, Variables.stamina)
    elif character.speed - character.move > 0:
        target_walk(character.coordinate, character.speed - character.move)
    for row in Variables.board:
        for place in row:
            if place.is_walkable:
                place.name = (str(place.x) + "," + str(place.y) + "(" + str(place.required_stamina) + ")")

    boardstate()
    action = input("Do you want to rush, walk or shoot (r=rush(4 stamina), (x,y)=walk, s=shoot(3 stamina), c=cancel or e=end turn:")
    while True:
        if "," in action:
            while True:
                if Variables.board[int(action[-1])][int(action[0])].is_walkable:
                    return character.walk_movement(Variables.board[int(action[-1])][int(action[0])], True, True)
                else:
                    boardstate()
                    action = input("Do you want to rush, walk or shoot (r=rush(4 stamina), (x,y)=walk, s=shoot(3 stamina), c=cancel or e=end turn:")
                    break
        elif action == "r":
            reset_board()
            if character.move == 0:
                target_walk(character.coordinate, character.speed + 2)
                for row in Variables.board:
                    for place in row:
                        if place.is_walkable:
                            place.name = (str(place.x) + "," + str(place.y))

                boardstate()

                action = input("Choose your destination (x,y):")
                while True:
                    if Variables.board[int(action[-1])][int(action[0])].is_walkable:
                        character.walk_movement(Variables.board[int(action[-1])][int(action[0])], False, True)
                        character.rushed = True
                        break
                    else:
                        boardstate()
                        action = input("Choose a valid destination (x,y):")

                character.move = character.speed

                reset_board()
                boardstate()
                return 4
            else:
                action = input("You can't rush if you already have moved. Choose a valid ability ((x,y)=walk, s=shoot, c=cancel or e=end turn:")

        elif action == "s":
            reset_board()
            if not character.shoot and not character.rushed and character.has_shield:
                if Variables.stamina < character.weapon.stamina_cost:
                    action = input("You don't have enough stamina to shoot. Choose a valid ability ((x,y)=walk, r=rush, c=cancel or e=end turn):")
                else:
                    return character.weapon.shoot()
            else:
                action = input("You can't shoot. Choose a valid ability ((x,y)=walk, r=rush, c=cancel or e=end turn):")
        elif action == "c":
            reset_board()
            return 0
        elif action == "e":
            reset_board()
            return 20
        else:
            action = input("Choose a valid ability (r=rush(4 stamina), (x,y)=walk, s=shoot(3 stamina), c=cancel or e=end turn:")


def deal_damage(shooter, target_of_damage, damage):
    reset_board()
    if not target_of_damage.has_shield:
        target_of_damage.health -= damage
        print(str(shooter)+" has dealt "+str(damage)+" damage to "+str(target_of_damage)+"! "+str(target_of_damage)+" has "+str(target_of_damage.health)+" health left.")
    else:
        target_of_damage.has_shield = False
        print(str(target_of_damage)+" has lost their shield. " + str(target_of_damage) + " has "+str(target_of_damage.health)+" health left.")


def alive():
    living = Variables.characters_alive
    for character in Variables.characters_alive:
        if character.health <= 0:
            print("Character " + str(character) + " has died.")
            living.remove(character)
            character.coordinate.character = None
    return living
