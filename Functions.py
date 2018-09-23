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
                    print((" " * int(floor(5 - (len(place.character.name) / 2))) + "(" + place.character.name + ")" + ceil(4 - (len(place.character.name) / 2)) * " "), end="")
                else:
                    print((" " * int(floor(6 - (len(place.character.name) / 2))) + place.character.name + ceil(5 - (len(place.character.name) / 2)) * " "), end="")
            elif len(place.areas) > 0:
                print((" " * int(floor(6 - (len(place.areas) / 2))) + "." * len(place.areas) + ceil(5 - (len(place.areas) / 2)) * " "), end="")
            elif place.is_cover:
                print((" " * 5 + str(place.health) + 5 * " "), end="")
            elif "," in place.name:
                index = place.name.index(",")
                print(" " * (5 - index) + place.name + " " * (6 - (len(place.name) - index)), end="")
            else:
                print((" " * int(floor(6 - (len(place.name) / 2))) + place.name + ceil(5 - (len(place.name) / 2)) * " "), end="")
        print("\n")


def set_graphic_board():
    for i in range(len(Variables.graphic_board)):
        for j in range(len(Variables.graphic_board[i])):
            Variables.graphic_board[i][j] = Variables.board[i + Variables.camera_movement_y][j + Variables.camera_movement_x]

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
    selected_character = input("Choose your character " + str(Variables.current_team.team_members_alive) + ":")
    while True:
        k = 0
        for character in Variables.current_team.team_members_alive:
            if str(character.name) == str(selected_character):
                return character
            else:
                k += 1
        if k == len(Variables.current_team.team_members_alive):
            selected_character = input("Please choose a valid character " + str(Variables.current_team.team_members_alive) + ":")


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
    if character.speed - character.has_moved > Variables.current_team.max_stamina - Variables.current_team.used_stamina:
        target_walk(character.coordinate, Variables.current_team.max_stamina - Variables.current_team.used_stamina)
    elif character.speed - character.has_moved > 0:
        target_walk(character.coordinate, character.speed - character.has_moved)
    for row in Variables.board:
        for place in row:
            if place.is_walkable:
                place.name = (str(place.x) + "," + str(place.y) + "(" + str(place.required_stamina) + ")")

    boardstate()
    action = input("Do you want to rush, walk or shoot (r=rush(4 stamina), (x,y)=walk, s=shoot(3 stamina), c=cancel or e=end turn:")
    while True:
        if "," in action:
            while True:
                if Variables.board[int(action.split(",")[-1])][int(action.split(",")[0])].is_walkable:
                    return character.walk_movement(Variables.board[int(action.split(",")[-1])][int(action.split(",")[0])], True, True)
                else:
                    boardstate()
                    action = input("Do you want to rush, walk or shoot (r=rush(4 stamina), (x,y)=walk, s=shoot(3 stamina), c=cancel or e=end turn:")
                    break
        elif action == "r":
            reset_board()
            if character.has_moved == 0:
                target_walk(character.coordinate, character.speed + 2)
                for row in Variables.board:
                    for place in row:
                        if place.is_walkable:
                            place.name = (str(place.x) + "," + str(place.y))

                boardstate()

                action = input("Choose your destination (x,y):")
                while True:
                    if "," in action:
                        if Variables.board[int(action.split(",")[-1])][int(action.split(",")[0])].is_walkable:
                            character.walk_movement(Variables.board[int(action.split(",")[-1])][int(action.split(",")[0])], False, True)
                            break
                        else:
                            boardstate()
                            action = input("Choose a valid destination (x,y):")
                    else:
                        boardstate()
                        action = input("Choose a valid destination (x,y):")

                character.has_rushed = True
                character.has_moved = character.speed

                reset_board()
                boardstate()
                return character.speed
            else:
                action = input("You can't rush if you already have moved. Choose a valid ability ((x,y)=walk, s=shoot, c=cancel or e=end turn:")

        elif action == "s":
            reset_board()
            if not character.has_shot and not character.has_rushed and character.has_shield:
                if Variables.current_team.max_stamina - Variables.current_team.used_stamina < character.weapon.stamina_cost:
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
            return Variables.current_team.max_stamina
        else:
            action = input("Choose a valid ability (r=rush(4 stamina), (x,y)=walk, s=shoot(3 stamina), c=cancel or e=end turn:")


def deal_damage(shooter, target_of_damage, damage, can_break_shield):
    reset_board()
    if not target_of_damage.has_shield:
        target_of_damage.health -= damage
        print(str(shooter)+" has dealt "+str(damage)+" damage to "+str(target_of_damage)+"! "+str(target_of_damage)+" has "+str(target_of_damage.health)+" health left.")
        alive()
    else:
        if can_break_shield:
            target_of_damage.has_shield = False
            print(str(target_of_damage)+" has lost their shield. " + str(target_of_damage) + " has "+str(target_of_damage.health)+" health left.")


def damage_cover(place, damage):
    place.health -= damage
    if place.health <= 0:
        place.is_cover = False


def alive():
    for team in Variables.teams:
        for character in team.team_members_alive:
            if character.health <= 0:
                print("Character " + str(character) + " has died.")
                team.team_members_alive.remove(character)
                character.coordinate.character = None
    win()


def win():
    for team in Variables.teams:
        if team.points >= 5 or len(Variables.teams[Variables.teams.index(Variables.current_team) - 1].team_members_alive) == 0:
            if len(Variables.current_team.team_members_alive) == 0:
                print("It's a tie!")
            else:
                print("Team " + str(Variables.current_team.team) + " wins!")
