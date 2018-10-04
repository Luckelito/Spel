def boardstate():
    inverted_board = reversed(Variables.board)
    print("")
    for row in inverted_board:
        for place in row:
            if type(place.character) == Classes.Character:
                if place.character.has_shield:
                    print((" " * int(floor(5 - (len(place.character.name) / 2))) + "(" + place.character.name + ")" + ceil(4 - (len(place.character.name) / 2)) * " "), end="")
                else:
                    print((" " * int(floor(6 - (len(place.character.name) / 2))) + place.character.name + ceil(5 - (len(place.character.name) / 2)) * " "), end="")
            elif len(place.areas) > 0:
                print((" " * int(floor(6 - (len(place.areas) / 2))) + "." * len(place.areas) + ceil(5 - (len(place.areas) / 2)) * " "), end="")
            elif place.is_cover:
                print((" " * 5 + str(place.health) + 5 * " "), end="")
            elif "," in place.name:
                index = place.name.index(",")
                print(" " * (5 - index) + place.name + " " * (6 - (len(place.name) - index)), end="")
            else:
                print((" " * int(floor(6 - (len(place.name) / 2))) + place.name + ceil(5 - (len(place.name) / 2)) * " "), end="")
        print("\n")