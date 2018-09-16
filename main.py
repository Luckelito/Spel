import Functions
from Variables import *
import Classes
from random import *

for team in teams:
    for character in team.team_members:
        Functions.equip(character, Classes.BasicWeapon)

for i in range(int((board_height * board_width)/10)):  # covers
    random_row = randint(1, int(board_height) - 2)
    random_col = randint(1, int(board_width) - 2)
    random_number = randint(1, 4)
    board[random_row][random_col].health = random_number
    board[random_row][random_col].is_cover = True
    board[random_row][random_col].is_open = False
    board[board_width - random_row][board_height - random_col].health = random_number
    board[board_width - random_row][board_height - random_col].name = board[board_width - random_row][board_height - random_col].health
    board[board_width - random_row][board_height - random_col].is_cover = True
    board[board_width - random_row][board_height - random_col].is_open = False


for i in range(-1, 2):  # capture points
    for j in range(-1, 2):
        Variables.board[int(board_height / 2 + i)][int(board_width / 2 + j)].is_capture_point = True
        Variables.board[int(board_height / 2 + i)][int(board_width / 2 + j)].is_cover = False
        Variables.board[int(board_height / 2 + i)][int(board_width / 2 + j)].health = 0
        Variables.board[int(board_height / 2 + i)][int(board_width / 2 + j)].name = "|_|"


# cover_list = [[1, 4], [1, 5], [0, 6]]
# for coordinate in cover_list:
#    cover = Classes.Cover(name=str(random.randint(1, 4)))
#    Functions.placement_swap(cover, coordinate[0], coordinate[-1])

Functions.starting_positions(int(board_height), int(board_width))

Functions.boardstate()

while True:
    for team in teams:
        max_stamina = 12
        if team.is_current_team:
            current_team = team

    for character in current_team.team_members_alive:
        character.has_moved = 0
        character.has_shot = False
        character.has_rushed = False
        character.has_shield = True
        for area in character.weapon.areas:
            area.remove(character.weapon)
        
    if current_team.team == 1:
        game_turn += 1
        
    if current_team.team == 2 and game_turn == 1:
        current_team.max_stamina = 15

    while current_team.used_stamina < current_team.max_stamina:
        print("It is player " + str(current_team.team) + "'s turn. You have " + str(current_team.max_stamina - current_team.used_stamina) + " stamina left.")
        current_team.used_stamina += Functions.turn(Functions.choose_character())

    current_team.is_current_team = False
    teams[teams.index(current_team) - 1].is_current_team = True
    current_team = teams[teams.index(current_team) - 1]

