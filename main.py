import Functions
import Variables
import Classes
from random import *

Functions.equip(Variables.A, Classes.BasicWeapon)
Functions.equip(Variables.a, Classes.BasicWeapon)
Functions.equip(Variables.B, Classes.CircleWeapon)
Functions.equip(Variables.a, Classes.CircleWeapon)
Functions.equip(Variables.C, Classes.SniperRifle)
Functions.equip(Variables.c, Classes.SniperRifle)

for i in range(int((Variables.board_height * Variables.board_width)/10)):  # covers
    random_row = randint(1, int(Variables.board_height) - 2)
    random_col = randint(1, int(Variables.board_width) - 2)
    random_number = randint(1, 4)
    Variables.board[random_row][random_col].health = random_number
    Variables.board[random_row][random_col].is_cover = True
    Variables.board[random_row][random_col].is_open = False
    Variables.board[Variables.board_width - random_row][Variables.board_height - random_col].health = random_number
    Variables.board[Variables.board_width - random_row][Variables.board_height - random_col].name = Variables.board[Variables.board_width - random_row][Variables.board_height - random_col].health
    Variables.board[Variables.board_width - random_row][Variables.board_height - random_col].is_cover = True
    Variables.board[Variables.board_width - random_row][Variables.board_height - random_col].is_open = False

for i in range(-1, 2):  # capture points
    for j in range(-1, 2):
        Variables.Variables.board[int(Variables.board_height / 2 + i)][int(Variables.board_width / 2 + j)].is_capture_point = True
        Variables.Variables.board[int(Variables.board_height / 2 + i)][int(Variables.board_width / 2 + j)].is_cover = False
        Variables.Variables.board[int(Variables.board_height / 2 + i)][int(Variables.board_width / 2 + j)].health = 0
        Variables.Variables.board[int(Variables.board_height / 2 + i)][int(Variables.board_width / 2 + j)].true_name = "|_|"
        Variables.Variables.board[int(Variables.board_height / 2 + i)][int(Variables.board_width / 2 + j)].name = "|_|"

# cover_list = [[1, 4], [1, 5], [0, 6]]
# for coordinate in cover_list:
#    cover = Classes.Cover(name=str(random.randint(1, 4)))
#    Functions.placement_swap(cover, coordinate[0], coordinate[-1])

Functions.starting_positions(int(Variables.board_height), int(Variables.board_width))

Functions.boardstate()

while True:
    for team in Variables.teams:
        team.max_stamina = 12
        team.used_stamina = 0

    for character in Variables.current_team.team_members_alive:
        character.has_moved = 0
        character.has_shot = False
        character.has_rushed = False
        character.has_shield = True
        for area in character.weapon.areas:
            character.weapon.areas.remove(area)
        
    if Variables.current_team.team == 1:
        Variables.game_turn += 1
        
    if Variables.current_team.team == 2 and Variables.game_turn == 1:
        Variables.current_team.max_stamina = 15

    while Variables.current_team.used_stamina < Variables.current_team.max_stamina:
        print("It is player " + str(Variables.current_team.team) + "'s turn. You have " + str(Variables.current_team.max_stamina - Variables.current_team.used_stamina) + " stamina left.")
        Variables.current_team.used_stamina += Functions.turn(Functions.choose_character())

    if Variables.current_team.team == 2 and Variables.game_turn == 1:
        for character in Variables.current_team.team_members_alive:
            character.has_rushed = False

    Variables.current_team.is_current_team = False
    Variables.teams[Variables.teams.index(Variables.current_team) - 1].is_current_team = True
    Variables.current_team = Variables.teams[Variables.teams.index(Variables.current_team) - 1]
    Variables.current_team.check_points()
    Functions.win()

