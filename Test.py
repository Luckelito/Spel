if Variables.board[int(action[-1])][int(action[0])].x - self.character.coordinate.x != 0:
    if place.x - self.character.coordinate.x != 0:
        if round((place.y - self.character.coordinate.y) / (place.x - self.character.coordinate.x)) == round(
                (Variables.board[int(action[-1])][int(action[0])].y - self.character.coordinate.y) / (
                        Variables.board[int(action[-1])][int(action[0])].x - self.character.coordinate.x)):
            if round(place.x - self.character.coordinate.x) / abs(
                    round(place.x - self.character.coordinate.x)) == round(
                    Variables.board[int(action[-1])][int(action[0])].x - self.character.coordinate.x) / abs(
                    round(Variables.board[int(action[-1])][int(action[0])].x - self.character.coordinate.x)):
                self.character.coordinate.is_shootable = True

else:
    if place.x - self.character.coordinate.x == 0:
        if round(place.y - self.character.coordinate.y) / abs(rou