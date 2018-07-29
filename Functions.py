from math import *
from random import *
import Variables
import Classes


def starting_positions(board_height, board_width):
    placement_swap(Variables.A, Variables.board[int(board_height/2 + 1)][0])
    placement_swap(Variables.B, Variables.board[int(board_height/2)][0])
    placement_swap(Variables.C, Variables.board[int(board_height/2 - 1)][0])
    placement_swap(Variables.a, Variables.board[int(board_height/2 + 1)][int(board_width - 1)])
    placement_swap(Variables.b, Variables.board[int(board_height/2)][int(board_width - 1)])
    placement_swap(Variables.c, Variables.board[int(board_height/2 - 1)][int(board_width - 1)])


def boardstate():
    inverted_board = reversed(Variables.board)
    for row in inverted_board:
        for place in row:
            if type(place.character) == Classes.Character:
                print((" " * int(floor(5 - (len(place.character.name) / 2))) + place.character.name + ceil(4 - (len(place.character.name) / 2)) * " "), end="")
            elif place.is_cover:
                print((" " * 4 + str(place.health) + 4 * " "), end="")
            elif "," in place.name:
                index = place.name.index(",")
                print(" " * (4 - index) + place.name + " " * (5 - (len(place.name) - index)), end="")
            else:
                print((" " * int(floor(5 - (len(place.name) / 2))) + place.name + ceil(4 - (len(place.name) / 2)) * " "), end="")
        print("\n")


def placement_swap(character, new_coordinate):
    if type(character.coordinate) == Classes.Coordinate:
        character.coordinate.character = None
    character.coordinate = new_coordinate
    new_coordinate.character = character


def choose_character():
    current_team = []
    for character in Variables.characters_alive:
        if character.team == Variables.players_turn:
            current_team.append(character)

    selected_character = input("Choose your character " + str(current_team) + ":")
    while 1 == 1:
        k = 0
        for character in current_team:
            if str(character.name) == str(selected_character):
                return character
            else:
                k += 1
        if k == len(current_team):
            selected_character = input("Please choose a valid character " + str(current_team) + ":")


def los_check(place, character_origin, delta_x, delta_y):  # delta_x and delta_y = -1 or 1
    if abs((place.y - character_origin.y) / (place.x - character_origin.x)) < 1:
        for i in range(int((int(character_origin.x - place.x) ** 2 + int(character_origin.y - place.y) ** 2) ** 0.5)):
            if (place.x - delta_x * i) != character_origin.x or int(place.y - delta_y * round(abs((place.y - character_origin.y) / (place.x - character_origin.x)) * i)) != character_origin.y:
                if Variables.board[int(place.y - delta_y * ceil(abs((place.y - character_origin.y) / (place.x - character_origin.x)) * i))][int(place.x - delta_x * i)].is_cover:
                    return
                if Variables.board[int(place.y - delta_y * floor(abs((place.y - character_origin.y) / (place.x - character_origin.x)) * i))][int(place.x - delta_x * i)].is_cover:
                    return
        place.is_los = True
    elif abs((place.y - character_origin.y) / (place.x - character_origin.x)) >= 1:
        for i in range(int((int(character_origin.y - place.y) ** 2 + int(character_origin.x - place.x) ** 2) ** 0.5)):
            if int(place.y - delta_y * i) != character_origin.y or int(place.x - delta_x * round(abs((place.x - character_origin.x) / (place.y - character_origin.y)) * i)) != character_origin.x:
                if Variables.board[int(place.y - delta_y * i)][int(place.x - delta_x * ceil(abs((place.x - character_origin.x) / (place.y - character_origin.y)) * i))].is_cover:
                    return
                if Variables.board[int(place.y - delta_y * i)][int(place.x - delta_x * floor(abs((place.x - character_origin.x) / (place.y - character_origin.y)) * i))].is_cover:
                    return
        place.is_los = True


def target_los(origin, ability_range):
    for row in Variables.board:
        for place in row:
            if ((origin.x - place.x) ** 2 + (origin.y - place.y) ** 2) ** 0.5 <= ability_range:
                place.los(origin)


def target_walk(origin, ability_range):
    legal_targets = [[], [], []]

    path_list = []
    for a in range(-1, 2, 1):
        for b in range(-1, 2, 1):
            for c in range(-1, 2, 1):
                for d in range(-1, 2, 1):
                    for e in range(-1, 2, 1):
                        for f in range(-1, 2, 1):
                            for g in range(-1, 2, 1):
                                for h in range(-1, 2, 1):
                                    path_list.append([a, b, c, d, e, f, g, h])

    for path_sublist in path_list:
        z = 0
        u = 0
        place = [0, 0]
        place[0] = origin.x
        place[1] = origin.y
        current_path = []
        while True:
            x = path_sublist[z]
            y = path_sublist[int(z+len(path_sublist)/2)]

            if place[0] + x == origin.x and place[1] + y == origin.y:
                break

            elif x != 0 and y != 0:
                if u <= ability_range - 2 ** 0.5:
                    if 0 <= place[0] + x <= Variables.board_width - 1 and 0 <= place[1] + y <= Variables.board_height - 1:
                        if not Variables.board[place[1] + y][place[0] + x].is_cover:
                            if 0 <= place[0] + 2 * x <= Variables.board_width - 1 and 0 <= place[1] + 2 * y <= Variables.board_height - 1:
                                place[0] += x
                                place[1] += y
                                current_path.append(place)
                                u += 2 ** 0.5
                                Variables.board[place[1]][place[0]].is_walkable = True
                                if u < Variables.board[place[1]][place[0]].required_stamina:
                                    Variables.board[place[1]][place[0]].required_stamina = ceil(u)
                                    Variables.board[place[1]][place[0]].path = current_path
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
                        current_path.append(place)
                        u += 1
                        Variables.board[place[1]][place[0]].is_walkable = True
                        if u < Variables.board[place[1]][place[0]].required_stamina:
                            Variables.board[place[1]][place[0]].required_stamina = ceil(u)
                            Variables.board[place[1]][place[0]].path = current_path
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
    if character.speed - character.move > 0:
        target_walk(character.coordinate, character.speed - character.move)
        for row in Variables.board:
            for place in row:
                if place.is_walkable:
                    if type(place.character) == Classes.Character:
                        place.character.name = (
                                    place.character.true_name + " " + str(place.x) + "," + str(place.y) + "(" + str(
                                place.required_stamina) + ")")
                    else:
                        place.name = (str(place.x) + "," + str(place.y) + "(" + str(place.required_stamina) + ")")
    boardstate()
    action = input("Do you want to rush, walk or shoot (r=rush(4 stamina), (x,y)=walk, s=shoot(3 stamina), c=cancel or e=end turn:")
    while True:
        if "," in action:
            while True:
                if Variables.board[int(action[-1])][int(action[0])].is_walkable:
                    placement_swap(character, Variables.board[int(action[-1])][int(action[0])])

                    moves = Variables.board[int(action[-1])][int(action[0])].required_stamina
                    character.move += moves

                    for row in Variables.board:
                        for place in row:
                            place.is_walkable = False
                            place.required_stamina = 100
                            place.path = []
                            place.name = place.true_name
                            if type(place.character) == Classes.Character:
                                place.character.name = place.character.true_name
                    boardstate()
                    return moves
                else:
                    boardstate()
                    action = input("Do you want to rush, walk or shoot (r=rush(4 stamina), (x,y)=walk, s=shoot(3 stamina), c=cancel or e=end turn:")
        elif action == "r":
            if character.move == 0:
                target_walk(character.coordinate, character.speed + 2)
                for row in Variables.board:
                    for place in row:
                        if place.is_walkable:
                            if type(place.character) == Classes.Character:
                                place.character.name = (place.character.true_name + " " + str(place.x) + "," + str(
                                    place.y) + "(" + str(place.required_stamina) + ")")
                            else:
                                place.name = (
                                            str(place.x) + "," + str(place.y) + "(" + str(place.required_stamina) + ")")
                character.move = character.speed

                for row in Variables.board:
                    for place in row:
                        place.is_walkable = False
                        place.required_stamina = 100
                        place.path = []
                        place.name = place.true_name
                        if type(place.character) == Classes.Character:
                            place.character.name = place.character.true_name
                return 4
            else:
                action = input("You can't rush if you already have moved. Choose a valid ability ((x,y)=walk, s=shoot, c=cancel or e=end turn:")
        elif action == "s":
            if not character.shoot:
                if Variables.stamina < 3:
                    action = input("You don't have enough stamina to shoot. Choose a valid ability ((x,y)=walk, r=rush, c=cancel or e=end turn):")
                else:
                    print("Bang!")
                    return 3
            else:
                action = input("You have already shoot. Choose a valid ability ((x,y)=walk, r=rush, c=cancel or e=end turn):")
        elif action == "c":
            return 0
        elif action == "e":
            return 20
        else:
            action = input("Choose a valid ability (r=rush(4 stamina), (x,y)=walk, s=shoot(3 stamina), c=cancel or e=end turn:")


def deal_damage(shooter, weapon, target):
    target.health -= weapon.damage
    print(str(shooter)+" has dealt "+str(weapon.damage)+" damage to "+str(target)+"! "+str(target)+" has "+str(target.health)+" health left.")


def alive():
    living = Variables.characters_alive
    for character in Variables.characters_alive:
        if character.health <= 0:
            print("Character " + str(character) + " has died.")
            living.remove(character)
            for row in Variables.board:
                for place in row:
                    if place == character.name:
                        Variables.board[Variables.board[row.index(place)]][row.index(place)].name = "_"
    return living
