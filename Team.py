from Classes import *
import Functions
import Variables


class Team:
    def __init__(self, team=None, is_current_team=False, team_members=[], team_members_alive=[], stamina=12, points=0):
        self.team = team
        self.is_current_team = is_current_team
        self.team_members = team_members
        self.team_members_alive = team_members_alive
        self.stamina = stamina
        self.points = points

    def check_points(self):
        i = 0
        j = 0

        for character in self.team_members_alive:
            if character.coordinate.is_capture_point:
                i += 1

        for character in Variables.teams[Variables.teams.index(self) - 1].team_members_alive:
            if character.coordinate.is_capture_point:
                j += 1

        if i > 0 and j == 0:
            self.points += 1

        print("Team " + str(Variables.teams[0].team) + " has " + str(Variables.teams[0].points) + " points.")
        print("Team " + str(Variables.teams[1].team) + " has " + str(Variables.teams[1].points) + " points.")
