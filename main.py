import Functions
import Variables
import Classes
import random

for i in range(int((Variables.n * Variables.m)**0.5)):
    random_row = random.randint(1, int(Variables.n) - 2)
    random_col = random.randint(1, int(Variables.m) - 2)
    if type(Variables.board[random_row][random_col]) == Classes.Open_ground:
        cover = Classes.Cover()
        cover.name = str(random.randint(1, 5))
        Functions.placement_swap(cover, random_col, random_row)
        Functions.placement_swap(cover, (-random_col - 1), (-random_row - 1))

Functions.starting_positions(int(Variables.n), int(Variables.m))

Functions.boardstate()

while 1 == 1:
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
        Variables.tot_moves += Functions.turn(Functions.chooseCharacter())
        Functions.alive()