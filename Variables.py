from Classes import *
import Functions

board_width = 15
board_height = 15

board = []
for i in range(int(board_height)):
    board.append([])
    for a in range(int(board_width)):
        board[i].append(Coordinate(true_name="_", name="_", health=0, x=a, y=i, is_cover=False, is_capture_point=False, is_open=True, is_los=False, is_in_range=False, is_walkable=False, required_stamina=100, path=[], character=None, areas=[]))

team_1 = Team(team=1, is_current_team=True, team_members=[], team_members_alive=[], used_stamina=0, max_stamina=12, points=0)
team_2 = Team(team=2, is_current_team=False, team_members=[], team_members_alive=[], used_stamina=0, max_stamina=12, points=0)
teams = [team_1, team_2]

game_turn = 0
current_team = team_1

A = Character(true_name="A", name="A", speed=4, health=220, team=team_1, move=0, shoot=False, rushed=False, coordinate=None, weapon=None, has_shield=True)
B = Character(true_name="B", name="B", speed=3, health=280, team=team_1, move=0, shoot=False, rushed=False, coordinate=None, weapon=None, has_shield=True)
C = Character(true_name="C", name="C", speed=3, health=180, team=team_1, move=0, shoot=False, rushed=False, coordinate=None, weapon=None, has_shield=True)
a = Character(true_name="a", name="a", speed=4, health=220, team=team_2, move=0, shoot=False, rushed=False, coordinate=None, weapon=None, has_shield=True)
b = Character(true_name="b", name="b", speed=3, health=280, team=team_2, move=0, shoot=False, rushed=False, coordinate=None, weapon=None, has_shield=True)
c = Character(true_name="c", name="c", speed=3, health=180, team=team_2, move=0, shoot=False, rushed=False, coordinate=None, weapon=None, has_shield=True)

team_1.team_members = [A, B, C]
team_2.team_members = [a, b, c]
team_1.team_members_alive = [A, B, C]
team_2.team_members_alive = [a, b, c]
