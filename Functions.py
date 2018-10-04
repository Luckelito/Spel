from math import *
from itertools import *
from random import *
import pygame
import os
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


def set_graphic_board():
    for row in Variables.board:
        for place in row:
            place.graphic_x_start = 0
            place.graphic_x_end = 0
            place.graphic_y_start = 0
            place.graphic_y_end = 0

    for i in range(len(Variables.graphic_board)):
        for j in range(len(Variables.graphic_board[i])):
            Variables.graphic_board[i][j] = Variables.board[i + Variables.camera_movement_y][j + Variables.camera_movement_x]
            Variables.graphic_board[i][j].graphic_x_start = 60 + j * 100
            Variables.graphic_board[i][j].graphic_x_end = 160 + j * 100
            Variables.graphic_board[i][j].graphic_y_start = 40 + i * 100
            Variables.graphic_board[i][j].graphic_y_end = 140 + i * 100


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


def choose_character():
    pressed_mouse = pygame.mouse.get_pressed()
    mouse_pos = pygame.mouse.get_pos()

    if pressed_mouse[0]:
        for row in Variables.graphic_board:
            for place in row:
                if place.graphic_x_start <= mouse_pos[0] < place.graphic_x_end and place.graphic_y_start <= mouse_pos[1] < place.graphic_y_end:
                    if type(place.character) == Classes.Character:
                        if place.character.team == Variables.current_team:
                            Variables.current_character = place.character

    return Variables.current_character


def turn(character):
    reset_board()

    if type(character) != Classes.Character:
        return 0


    if character.speed - character.has_moved > Variables.current_team.max_stamina - Variables.current_team.used_stamina:
        target_walk(character.coordinate, Variables.current_team.max_stamina - Variables.current_team.used_stamina)
    elif character.speed - character.has_moved > 0:
        target_walk(character.coordinate, character.speed - character.has_moved)
    for row in Variables.board:
        for place in row:
            if place.is_walkable:
                place.name = (str(place.x) + "," + str(place.y) + "(" + str(place.required_stamina) + ")")

    
    pressed_key = pygame.key.get_pressed()
    pressed_mouse = pygame.mouse.get_pressed()
    mouse_pos = pygame.mouse.get_pos()

    if pressed_key[pygame.K_r]:
        reset_board()
        if character.has_moved == 0:
            target_walk(character.coordinate, character.speed + 2)
            for row in Variables.board:
                for place in row:
                    if place.is_walkable:
                        place.name = (str(place.x) + "," + str(place.y))

            

            for row in Variables.board:
                for place in row:
                    if place.graphic_x_start <= mouse_pos[0] < place.graphic_x_end and place.graphic_y_start <= mouse_pos[1] < place.graphic_y_end:
                        if Variables.board[int(place.y)][int(place.x)].is_walkable:
                            return character.walk_movement(Variables.board[int(place.y)][int(place.x)], True, True)

            character.has_rushed = True
            character.has_moved = character.speed

            reset_board()
            
            return character.speed

    elif pressed_mouse[0]:
        for row in Variables.board:
            for place in row:
                if place.graphic_x_start <= mouse_pos[0] < place.graphic_x_end and place.graphic_y_start <= mouse_pos[1] < place.graphic_y_end:
                    if Variables.board[int(place.y)][int(place.x)].is_walkable:
                        return character.walk_movement(Variables.board[int(place.y)][int(place.x)], True, True)

    elif pressed_key[pygame.K_s]:
        reset_board()
        if not character.has_shot and not character.has_rushed and character.has_shield:
            if Variables.current_team.max_stamina - Variables.current_team.used_stamina > character.weapon.stamina_cost:
                return character.weapon.shoot()

    elif pressed_key[pygame.K_ESCAPE]:
        reset_board()
        Variables.current_character = None
        return 0

    elif pressed_key[pygame.K_e]:
        reset_board()
        return Variables.current_team.max_stamina

    return 0


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
