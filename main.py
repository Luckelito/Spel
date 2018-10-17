import Functions
import Variables
import Classes
import pygame
import Graphics
import os
from random import *
pygame.init()
Variables.passed_time = pygame.time.get_ticks()

Functions.equip(Variables.A, Classes.BasicWeapon)
Functions.equip(Variables.a, Classes.BasicWeapon)
Functions.equip(Variables.B, Classes.BasicWeapon)
Functions.equip(Variables.b, Classes.BasicWeapon)
Functions.equip(Variables.C, Classes.BasicWeapon)
Functions.equip(Variables.c, Classes.BasicWeapon)

#for i in range(int((Variables.board_height * Variables.board_width)/10)):  # covers
 #   random_y = randint(1, int(Variables.board_height) - 2)
  #  random_x = randint(1, int(Variables.board_width) - 2)
   # random_number = randint(1, 4)
#    Variables.board[random_y][random_x].health = random_number
 #   Variables.board[random_y][random_x].is_cover = True
  #  Variables.board[random_y][random_x].is_open = False
   # Variables.board[Variables.board_height - random_y - 1][Variables.board_width - random_x - 1].health = random_number
#    Variables.board[Variables.board_height - random_y - 1][Variables.board_width - random_x - 1].name = Variables.board[Variables.board_height - random_y][Variables.board_width - random_x].health
 #   Variables.board[Variables.board_height - random_y - 1][Variables.board_width - random_x - 1].is_cover = True
  #  Variables.board[Variables.board_height - random_y - 1][Variables.board_width - random_x - 1].is_open = False

for i in range(-1, 2):  # capture points
    for j in range(-1, 2):
        Variables.Variables.board[int(Variables.board_height / 2 + i)][int(Variables.board_width / 2 + j)].is_capture_point = True
        Variables.Variables.board[int(Variables.board_height / 2 + i)][int(Variables.board_width / 2 + j)].is_cover = False
        Variables.Variables.board[int(Variables.board_height / 2 + i)][int(Variables.board_width / 2 + j)].health = 0

# cover_list = [[1, 4], [1, 5], [0, 6]]
# for coordinate in cover_list:
#    cover = Classes.Cover(name=str(random.randint(1, 4)))
#    Functions.placement_swap(cover, coordinate[0], coordinate[-1])

Functions.starting_positions(int(Variables.board_height), int(Variables.board_width))

clock = pygame.time.Clock()

all_fonts = pygame.font.get_fonts()
font = pygame.font.Font(None, 100)

pygame.init()
screen = pygame.display.set_mode((1920, 1080))
done = False

for team in Variables.teams:
    team.max_stamina = 12
    team.used_stamina = 0

while not done:
    if Variables.current_team.team == 1:
        Variables.game_turn += 1

    if not Variables.current_team.used_stamina < Variables.current_team.max_stamina:
        Variables.current_team.is_current_team = False
        Variables.teams[Variables.teams.index(Variables.current_team) - 1].is_current_team = True
        Variables.current_team = Variables.teams[Variables.teams.index(Variables.current_team) - 1]
        Variables.current_team.check_points()
        Variables.current_character = None
        for team in Variables.teams:
            team.max_stamina = 12
            team.used_stamina = 0
        for character in Variables.current_team.team_members_alive:
            character.has_moved = 0
            character.has_shot = False
            character.has_rushed = False
            character.has_shield = True

            areas_to_remove = []
            for place in character.weapon.areas:
                if len(character.weapon.areas) > 0:
                    place.areas.remove(character.weapon)
                    areas_to_remove.append(place)
            for place in areas_to_remove:
                if len(areas_to_remove) > 0:
                    character.weapon.areas.remove(place)

    if Variables.current_team.team == 2 and Variables.game_turn == 1:
        Variables.current_team.max_stamina = 15
        for character in Variables.current_team.team_members_alive:
            character.has_rushed = False

    Functions.win()

    Variables.current_team.used_stamina += Functions.turn(Functions.choose_character())

    Functions.set_graphic_board()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    Graphics.graphics(screen, font)

    pygame.display.flip()
    clock.tick(60)

