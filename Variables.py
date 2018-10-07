from Classes import *
import Functions

board_width = 21
board_height = 15

board = []
for i in range(int(board_height)):
    board.append([])
    for a in range(int(board_width)):
        board[i].append(Coordinate(health=0, x=a, y=i, is_cover=False, is_capture_point=False, required_stamina=100, path=[], character=None, areas=[]))

graphic_width = 18
graphic_height = 10
camera_movement_y = int(board_height/2) - 5
camera_movement_x = 0

graphic_board = []
for i in range(int(graphic_height)):
    graphic_board.append([])
    for a in range(int(graphic_width)):
        graphic_board[i].append(None)

team_1 = Team(team=1, is_current_team=True)
team_2 = Team(team=2, is_current_team=False)
teams = [team_1, team_2]

A = Character(name="A", team=team_1)
B = Character(name="B", team=team_1)
C = Character(name="C", team=team_1)
a = Character(name="a", team=team_2)
b = Character(name="b", team=team_2)
c = Character(name="c", team=team_2)

team_1.team_members = [A, B, C]
team_2.team_members = [a, b, c]
team_1.team_members_alive = [A, B, C]
team_2.team_members_alive = [a, b, c]

game_turn = 0
current_team = team_1
current_character = None
