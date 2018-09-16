from Classes import *
import Functions
import Variables


class Team:
    def __init__(self, team, is_current_team, team_members, team_members_alive, used_stamina, max_stamina, points):
        self.team = team
        self.is_current_team = is_current_team
        self.team_members = team_members
        self.team_members_alive = team_members_alive
        self.used_stamina = used_stamina
        self.max_stamina = max_stamina
        self.points = points

    def check_points(self):
        i = 0
        for character in self.team_members:
            if character.coordinate.is_capture_point:
                i += 1

        return i
