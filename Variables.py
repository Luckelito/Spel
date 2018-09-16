from Classes import *
import Functions

board_width = 9
board_height = 9

board = []
for i in range(int(board_height)):
    board.append([])
    for a in range(int(board_width)):
        board[i].append(Coordinate(true_name="_", name="_", health=0, x=a, y=i, is_cover=False, is_open=True, is_los=False, is_in_range=False, is_walkable=False, required_stamina=100, path=[], character=None, areas=[]))

players_turn = 1
game_turn = 0
stamina = 12

A = Character(true_name="A", name="A", speed=4, health=220, team=1, move=0, shoot=False, rushed=False, coordinate=None, weapon=None, has_shield=True)
B = Character(true_name="B", name="B", speed=3, health=280, team=1, move=0, shoot=False, rushed=False, coordinate=None, weapon=None, has_shield=True)
C = Character(true_name="C", name="C", speed=3, health=180, team=1, move=0, shoot=False, rushed=False, coordinate=None, weapon=None, has_shield=True)
a = Character(true_name="a", name="a", speed=4, health=220, team=2, move=0, shoot=False, rushed=False, coordinate=None, weapon=None, has_shield=True)
b = Character(true_name="b", name="b", speed=3, health=280, team=2, move=0, shoot=False, rushed=False, coordinate=None, weapon=None, has_shield=True)
c = Character(true_name="c", name="c", speed=3, health=180, team=2, move=0, shoot=False, rushed=False, coordinate=None, weapon=None, has_shield=True)

characters_alive = [A, B, C, a, b, c]
