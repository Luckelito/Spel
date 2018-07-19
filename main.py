import Functions
import Variables
import Classes
import random

# for i in range(int((Variables.board_height * Variables.board_width)/5)):
#    random_row = random.randint(1, int(Variables.board_height) - 2)
#    random_col = random.randint(1, int(Variables.board_width) - 2)
#    if type(Variables.board[random_row][random_col]) == Classes.Open_ground:
#        cover = Classes.Cover()
#        cover.name = str(random.randint(1, 4))
#        Functions.placement_swap(cover, random_col, random_row)
#        Functions.placement_swap(cover, (-random_col - 1), (-random_row - 1))

 # test covers
cover_list = [[1, 4], [1, 5], [0, 6]]
for coordinate in cover_list:
    cover = Classes.Cover()
    cover.name = str(random.randint(1, 4))
    Functions.placement_swap(cover, coordinate[0], coordinate[-1])

Functions.starting_positions(int(Variables.board_height), int(Variables.board_width))

Functions.boardstate()

while True:
    if Variables.players_turn > 1:
        Variables.players_turn -= 1

    else:
        Variables.players_turn += 1

    for character in Variables.characters_alive:
        character.move = 0
        character.shoot = 0

    if Variables.players_turn == 1:
        Variables.game_turn += 1

    if Variables.players_turn == 2 and Variables.game_turn == 1:
        Variables.tot_moves = -1
    else:
        Variables.tot_moves = 0
    while Variables.tot_moves < 3:
        print("It is player " + str(Variables.players_turn) + "'s turn. You have " + str(3 - Variables.tot_moves) + " moves left.")
        Variables.tot_moves += Functions.turn(Functions.choose_character())
        Functions.alive()
