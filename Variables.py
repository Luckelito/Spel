from Classes import *
import Functions

board_width = 15
board_height = 15

board = []
for i in range(int(board_height)):
    board.append([])
    for a in range(int(board_width)):
        board[i].append(Coordinate(true_name="_", name="_", health=0, x=a, y=i, is_cover=False, is_capture_point=False, is_open=True, is_los=False, is_in_range=False, is_walkable=False, required_stamina=100, path=[], character=None, areas=[]))

team_1 = Team(team=1, is_current_team=True)
team_2 = Team(team=2, is_current_team=False)
teams = [team_1, team_2]

A = Character(true_name="A", name="A", team=team_1)
B = Character(true_name="B", name="B", team=team_1)
C = Character(true_name="C", name="C", team=team_1)
a = Character(true_name="a", name="a", team=team_2)
b = Character(true_name="b", name="b", team=team_2)
c = Character(true_name="c", name="c", team=team_2)

team_1.team_members = [A, B, C]
team_2.team_members = [a, b, c]
team_1.team_members_alive = [A, B, C]
team_2.team_members_alive = [a, b, c]

game_turn = 0
current_team = team_1
