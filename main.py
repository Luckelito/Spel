import Functions
import Variables
import Classes

# for i in range(10):
# random_number = random.randint(1, 5)
# random_row = random.randint(1, int(n) - 2)
# random_col = random.randint(1, int(m) - 2)
# if board[random_row][random_col] == "_":
# Functions.placement_swap(str(random_number), random_col, random_row)
# Functions.placement_swap(str(random_number), (-random_col - 1), (-random_row - 1))

# Functions.placement_swap("TEST", 3, 5)
Functions.placement_swap("TEST", 3, 4)
Functions.placement_swap("TEST", 3, 3)
# Functions.placement_swap("TEST", 4, 3)
Functions.placement_swap("TEST", 5, 3)
# Functions.placement_swap("TEST", 5, 4)
# Functions.placement_swap("TEST", 5, 5)
Functions.placement_swap("TEST", 4, 5)


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