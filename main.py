import Functions
import Variables
import Classes
from random import *

for character in Variables.characters_alive:
    Functions.equip(character, Classes.BasicWeapon)

for i in range(int((Variables.board_height * Variables.board_width)/5)):
    random_row = randint(1, int(Variables.board_height) - 2)
    random_col = randint(1, int(Variables.board_width) - 2)
    random_number = randint(1, 4)
    Variables.board[random_row][random_col].health = random_number
    Variables.board[random_row][random_col].name = Variables.board[random_row][random_col].health
    Variables.board[random_row][random_col].is_cover = True
    Variables.board[Variables.board_width - random_row][Variables.board_height - random_col].health = random_number
    Variables.board[Variables.board_width - random_row][Variables.board_height - random_col].name = Variables.board[Variables.board_width - random_row][Variables.board_height - random_col].health
    Variables.board[Variables.board_width - random_row][Variables.board_height - random_col].is_cover = True

# cover_list = [[1, 4], [1, 5], [0, 6]]
# for coordinate in cover_list:
#    cover = Classes.Cover(name=str(random.randint(1, 4)))
#    Functions.placement_swap(cover, coordinate[0], coordinate[-1])

Functions.starting_positions(int(Variables.board_height), int(Variables.board_width))

Functions.boardstate()

while True:

    for character in Variables.characters_alive:
        character.move = 0
        character.shoot = False

    if Variables.players_turn == 1:
        Variables.game_turn += 1

    if Variables.players_turn == 2 and Variables.game_turn == 1:
        Variables.stamina = 15

    while Variables.stamina > 0:
        print("It is player " + str(Variables.players_turn) + "'s turn. You have " + str(Variables.stamina) + " stamina left.")
        Variables.stamina -= Functions.turn(Functions.choose_character())
        Functions.alive()

    if Variables.players_turn > 1:
        Variables.players_turn -= 1

    else:
        Variables.players_turn += 1
