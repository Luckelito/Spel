import math
import random
import Variables
import Classes

def starting_positions(board_height, board_width):
  placement_swap(Variables.A, 4, 4)
  placement_swap(Variables.B, 0, 0)
  placement_swap(Variables.C, 0, 1)
  placement_swap(Variables.a, (board_width - 2), (board_height - 1))
  placement_swap(Variables.b, (board_width - 1), (board_height - 1))
  placement_swap(Variables.c, (board_width - 1), (board_height - 2))

def boardstate():
  inverted_board = reversed(Variables.board)
  for row in inverted_board:
    for place in row:
        if type(place) == Classes.Character:
            print("   " + place.name + "   ", end="")
        elif "," in place:
            index = place.index(",")
            print(" " * (3 - index) + place + " " * (4 -(len(place) - index)), end="")
        else:
            print((" " * int(math.floor(4 - (len(place) / 2))) + place + math.ceil(3 - (len(place) / 2)) * " "), end="")
    print("\n")

def placement_swap(character, x_coordinate, y_coordinate):
    Variables.board[y_coordinate][x_coordinate] = character

def character_coordinates(character):
    for row in Variables.board:
        for position in row:
            if position == character:
                return (row.index(position), Variables.board.index(row))

def chooseCharacter():
  current_team = []
  for character in Variables.characters_alive:
    if character.team == Variables.players_turn:
      current_team.append(character)

  selected_character = input("Choose your character " + str(current_team) + ":")
  while 1 == 1:
    k = 0
    for character in current_team:
      if str(character.name) == str(selected_character):
        return character
      else:
        k+=1
    if k == len(current_team):
      selected_character = input("Please choose a valid character " + str(current_team) + ":")

#def target(origin, ability_range, target_1, target_2, other_characters):#parameter = "ally" or "enemy"
#  y = 0
#  legal_targets_1 = []
#  legal_targets_2 = []
#  legal_targets_3 = []
#  legal_targets = [legal_targets_1, legal_targets_2, legal_targets_3]
#
#  while 1 == 1:
#    for y in range(ability_range):
#     for targets in legal_targets:
#        for i in range(-1,1,2):
#          if board[target[0]] == 1:
#            print("HEJ")
#  return (legal_targets)

def different_targets(place,output_list,x_coordinate,y_coordinate,target_1,target_2,other_characters):
    if place == target_1:
        output_list[0].append([x_coordinate, y_coordinate])
    elif place == target_2:
        output_list[1].append([x_coordinate, y_coordinate])
    elif other_characters == "ally" and type(place) == Classes.Character:
        if place.team == Variables.players_turn:
            output_list[2].append([x_coordinate, y_coordinate])
    elif other_characters == "enemy" and type(place) == Classes.Character:
        if place.team != Variables.players_turn:
            output_list[2].append([x_coordinate, y_coordinate])
    elif other_characters == "all" and type(place) == Classes.Character:
        output_list[2].append([x_coordinate, y_coordinate])

def LoS_check(coordinates, coordinates_origin, illegal_list, target_1, target_2, other_characters, delta_x, delta_y): # delta_x and delta_y = -1 or 1
    if abs((coordinates[-1] - coordinates_origin[-1]) / (coordinates[0] - coordinates_origin[0])) < 1:
        for i in range(int((int(coordinates_origin[0] - coordinates[0]) ** 2 + int(coordinates_origin[-1] - coordinates[-1]) ** 2) ** 0.5)):
            if (coordinates[0] - delta_x * i) != coordinates_origin[0] or int(coordinates[-1] - delta_y * round(abs((coordinates[-1] - coordinates_origin[-1]) / (coordinates[0] - coordinates_origin[0])) * i)) != coordinates_origin[-1]:
                if Variables.board[int(coordinates[-1] - delta_y * math.ceil(abs((coordinates[-1] - coordinates_origin[-1]) / (coordinates[0] - coordinates_origin[0])) * i))][int(coordinates[0] - delta_x * i)] != "_" and Variables.board[int(coordinates[-1] - delta_y * math.floor(abs((coordinates[-1] - coordinates_origin[-1]) / (coordinates[0] - coordinates_origin[0])) * i))][int(coordinates[0] - delta_x * i)]:
                    for k in range(i):
                        different_targets(Variables.board[int(coordinates[-1] - delta_y * math.ceil(abs((coordinates[-1] - coordinates_origin[-1]) / (coordinates[0] - coordinates_origin[0])) * k))][int(coordinates[0] - delta_x * k)], illegal_list, int(coordinates[0] - delta_x * k), int(coordinates[-1] - delta_y * math.ceil(abs((coordinates[-1] - coordinates_origin[-1]) / (coordinates[0] - coordinates_origin[0])) * k)), target_1, target_2, other_characters)
                    return
                if Variables.board[int(coordinates[-1] - delta_y * math.floor(abs((coordinates[-1] - coordinates_origin[-1]) / (coordinates[0] - coordinates_origin[0])) * i))][int(coordinates[0] - delta_x * i)] != "_" and Variables.board[int(coordinates[-1] - delta_y * math.floor(abs((coordinates[-1] - coordinates_origin[-1]) / (coordinates[0] - coordinates_origin[0])) * i))][int(coordinates[0] - delta_x * i)]:
                    for k in range(i):
                        different_targets(Variables.board[int(coordinates[-1] - delta_y * math.floor(abs((coordinates[-1] - coordinates_origin[-1]) / (coordinates[0] - coordinates_origin[0])) * k))][int(coordinates[0] - delta_x * k)], illegal_list,int(coordinates[0] - delta_x * k), int(coordinates[-1] - delta_y * math.floor(abs((coordinates[-1] - coordinates_origin[-1]) / (coordinates[0] - coordinates_origin[0])) * k)), target_1, target_2, other_characters)
                    return
    elif abs((coordinates[-1] - coordinates_origin[-1]) / (coordinates[0] - coordinates_origin[0])) >= 1:
        for i in range(int((int(coordinates_origin[-1] - coordinates[-1]) ** 2 + int(coordinates_origin[0] - coordinates[0]) ** 2) ** 0.5)):
            if int(coordinates[-1] - delta_y * i) != coordinates_origin[-1] or int(coordinates[0] - delta_x * round(abs((coordinates[0] - coordinates_origin[0]) / (coordinates[-1] - coordinates_origin[-1])) * i)) != coordinates_origin[0]:
                if Variables.board[int(coordinates[-1] - delta_y * i)][int(coordinates[0] - delta_x * math.ceil(abs((coordinates[0] - coordinates_origin[0]) / (coordinates[-1] - coordinates_origin[-1])) * i))] != "_":
                    for k in range(i):
                        different_targets(Variables.board[int(coordinates[-1] - delta_y * k)][int(coordinates[0] - delta_x * math.ceil(abs((coordinates[0] - coordinates_origin[0]) / (coordinates[-1] - coordinates_origin[-1])) * k))], illegal_list, int(coordinates[0] - delta_x * math.ceil(abs((coordinates[0] - coordinates_origin[0]) / (coordinates[-1] - coordinates_origin[-1])) * k)), (coordinates[-1] - delta_y * k), target_1, target_2, other_characters)
                    return
                if Variables.board[int(coordinates[-1] - delta_y * i)][int(coordinates[0] - delta_x * math.floor(abs((coordinates[0] - coordinates_origin[0]) / (coordinates[-1] - coordinates_origin[-1])) * i))] != "_":
                    for k in range(i):
                        different_targets(Variables.board[int(coordinates[-1] - delta_y * k)][int(coordinates[0] - delta_x * math.floor(abs((coordinates[0] - coordinates_origin[0]) / (coordinates[-1] - coordinates_origin[-1])) * k))], illegal_list, int(coordinates[0] - delta_x * math.floor(abs((coordinates[0] - coordinates_origin[0]) / (coordinates[-1] - coordinates_origin[-1])) * k)), (coordinates[-1] - delta_y * k), target_1, target_2, other_characters)
                    return

def LoS_check_2(place, origin, illegal_targets, target_1, target_2, other_characters):
    if place[0]-origin[0] > 0 and place[-1]-origin[-1] > 0:
        LoS_check(place, origin, illegal_targets, target_1, target_2, other_characters, 1, 1)
    elif place[0]-origin[0] < 0 and place[-1]-origin[-1] < 0:
        LoS_check(place, origin, illegal_targets, target_1, target_2, other_characters, -1, -1)
    elif place[0]-origin[0] > 0 and place[-1]-origin[-1] < 0:
        LoS_check(place, origin, illegal_targets, target_1, target_2, other_characters, 1, -1)
    elif place[0]-origin[0] < 0 and place[-1]-origin[-1] > 0:
        LoS_check(place, origin, illegal_targets, target_1, target_2, other_characters, -1, 1)
    elif place[0]-origin[0] == 0 and place[-1]-origin[-1] > 0:
        for i in range(int((int(origin[-1] - place[-1])**2 + int(origin[0] - place[0])**2)**0.5)+1):
            if (place[-1]-i) != origin[-1] or (place[0]-(place[0]-origin[0])/(place[-1]-origin[-1])*i) != origin[0]:
                if Variables.board[int(place[-1]-i)][int(place[0])] != "_":
                    for k in range(i):
                        different_targets(Variables.board[int(place[-1]-k)][int(place[0])], illegal_targets, int(place[0]), int(place[-1]-k), target_1, target_2, other_characters)
                    break
    elif place[0]-origin[0] == 0 and place[-1]-origin[-1] < 0:
        for i in range(int((int(origin[-1] - place[-1])**2 + int(origin[0] - place[0])**2)**0.5)+1):
            if (place[-1]+i) != origin[-1] or (place[0]+(place[0]-origin[0])/(place[-1]-origin[-1])*i) != origin[0]:
                if Variables.board[int(place[-1]+i)][int(place[0])] != "_":
                    for k in range(i):
                        different_targets(Variables.board[int(place[-1]+k)][int(place[0])], illegal_targets, int(place[0]), int(place[-1]+k), target_1, target_2, other_characters)
                    break
    elif place[-1]-origin[-1] == 0 and place[0]-origin[0] > 0:
        for i in range(int((int(origin[-1] - place[-1])**2 + int(origin[0] - place[0])**2)**0.5)+1):
            if (place[0]-i) != origin[0]:
                if Variables.board[int(place[-1])][int(place[0]-i)] != "_":
                    for k in range(i):
                        different_targets(Variables.board[int(place[-1])][int(place[0]-k)], illegal_targets, int(place[0]-k), int(place[-1]), target_1, target_2, other_characters)
                    break
    elif place[-1]-origin[-1] == 0 and place[0]-origin[0] < 0:
        for i in range(int((int(origin[-1] - place[-1])**2 + int(origin[0] - place[0])**2)**0.5)+1):
            if (place[0]+i) != origin[0]:
                if Variables.board[int(place[-1])][int(place[0]+i)] != "_":
                    for k in range(i):
                        different_targets(Variables.board[int(place[-1])][int(place[0]+k)], illegal_targets, int(place[0]+k), int(place[-1]), target_1, target_2, other_characters)
                    break


    list1 = [[], [], []]

    for lista in illegal_targets:
        for place in lista:
            k = 0
            for place_1 in list1[illegal_targets.index(lista)]:
                if place == place_1:
                    k += 1
            if k == 0:
                for i in range(len(lista)):
                    if place == lista[i] and lista.index(place) != i:
                        list1[illegal_targets.index(lista)].append(lista[i])

    for lista in list1:
        for place in lista:
            illegal_targets[list1.index(lista)].remove(place)

def target_LoS(origin, ability_range, target_1, target_2, other_characters): #parameter = "all","ally" or "enemy"
    y = 0
    legal_targets = [[], [], []]
    for row in Variables.board:
        x = 0
        for column in row:
            if ((origin[0] - x)**2 + (origin[-1] - y)**2)**0.5 <= ability_range:
                different_targets(column, legal_targets, x, y, target_1, target_2, other_characters)
            x += 1
        y += 1

    illegal_targets = [[], [], []]
    cover_los = 1

    for lista in legal_targets:
        for place in lista:
            for i in range(-1, 2, 2):
                LoS_check_2(place, origin, illegal_targets, target_1, target_2, other_characters)
                if Variables.board[place[-1]][place[0] + i] != "_":
                    for k in range(-1, 2, 2):
                        if Variables.board[place[-1] + k][place[0]] != "_":
                            LoS_check_2((place[-1] + k, place[0]), origin, illegal_targets, target_1, target_2, other_characters)
                            cover_los += 1
                if Variables.board[place[-1] + i][place[0]] != "_":
                    for k in range(-1, 2, 2):
                        if Variables.board[place[-1]][place[0] + k] != "_":
                            LoS_check_2((place[-1], place[0] + k), origin, illegal_targets, target_1, target_2, other_characters)
                            cover_los += 1

    list1 = [[], [], []]


    for lista in illegal_targets:
        for place in lista:
            a = 0
            for i in range(len(lista)):
                if place == lista[i]:
                    a += 1
            if a < cover_los:
                list1[illegal_targets.index(lista)].append(place)

    for lista in list1:
        for place in lista:
            illegal_targets[list1.index(lista)].remove(place)

    list1 = [[], [], []]

    for lista in illegal_targets:
        for place in lista:
            k = 0
            for place_1 in list1[illegal_targets.index(lista)]:
                if place == place_1:
                    k += 1
            if k == 0:
                for i in range(len(lista)):
                    if place == lista[i] and lista.index(place) != i:
                        list1[illegal_targets.index(lista)].append(lista[i])

    for lista in list1:
        for place in lista:
            illegal_targets[list1.index(lista)].remove(place)

    for lista in illegal_targets:
        for place in lista:
            legal_targets[illegal_targets.index(lista)].remove(place)

    return legal_targets

def walk(character):
    if character.move == 1:
        print("This character has already moved this turn, please choose another!")
        return 0
    else:
        moves = 0
        coordinate = character_coordinates(character)
        movement = input("Do you want to rush or walk (r=rush or w=walk):")
        while 1 == 1:
            if movement == "w":
                legal_destination = target_LoS(coordinate, character.speed, "_", "_","ally")
                moves += 1
                character.move = 1
                break
            elif movement == "r" and Variables.tot_moves < 2:
                print (moves)
                legal_destination = target_LoS(coordinate, (character.speed + 2), "_", "_", "ally")
                moves += 2
                character.move = 1
                break
            elif movement == "cancel":
                return 0
            else:
                movement = input("Choose a valid ability (r,w or cancel). Make sure you have enough moves left for the desired move:")

    for legal_coordinate in legal_destination[0]:
        placement_swap(str(legal_coordinate[0]) + "," + str(legal_coordinate[-1]),int(legal_coordinate[0]), int(legal_coordinate[-1]))

    boardstate()
    destination = input("Choose destination (x,y)").split(",")
    while 1 == 1:
        e = 0
        for legal_coordinate in legal_destination[0]:
            if str(destination[0]) == str(legal_coordinate[0]) and str(destination[-1]) == str(legal_coordinate[-1]):
                legal_destination[0].remove(legal_coordinate)
                e += 1
        if e == 1:
            placement_swap(character, int(destination[0]), int(destination[-1]))
            placement_swap("_", coordinate[0], coordinate[-1])
            break
        else:
            boardstate()
            destination = input("Choose a valid destination (x,y)")

    for legal_coordinate in legal_destination[0]:
        placement_swap("_", int(legal_coordinate[0]), int(legal_coordinate[-1]))

    boardstate()

    return int(moves)

def shoot(character):
    if character.shoot == 1:
        print("This character has already shot this turn, please choose another!")
        return 0
    else:
        moves = 0
        chosen_weapon = input("Choose your weapon (1="+str(character.weapon_1)+" or 2="+str(character.weapon_2)+"):")
    while 1 == 1:
        if chosen_weapon == "1":
            chosen_weapon = character.weapon_1
            break
        elif chosen_weapon == "2":
            chosen_weapon = character.weapon_2
            break
        elif chosen_weapon == "cancel":
            return 0
        else:
            chosen_weapon = input("Choose a valid weapon:")
    list1 = []
    old_names = []
    for i in range(int(1/chosen_weapon.dropoff)):
        accuracy_list = target_LoS(character_coordinates(character), (chosen_weapon.range_ + i), "_", "_", "enemy")
        for accuracy_place in accuracy_list[0]:
            if (100 - chosen_weapon.dropoff * i * 100) > 0:
                placement_swap((str(round(100 - chosen_weapon.dropoff * i * 100)) + "%"),int(accuracy_place[0]), int(accuracy_place[-1]))
                list1.append(accuracy_place)
        if len(accuracy_list[2]) > 0:
            for accuracy_place in accuracy_list[2]:
                old_names.append(Variables.board[accuracy_place[1]][accuracy_place[0]].name)
                Variables.board[accuracy_place[1]][accuracy_place[0]].name = (old_names[-1]+" "+str(100-100 * chosen_weapon.dropoff * (((character_coordinates(character)[0] - accuracy_place[0])**2 + (character_coordinates(character)[-1] - accuracy_place[1])**2)**0.5-chosen_weapon.range_)))
    boardstate()

    if len(accuracy_list[2])>0:
        target_character = input("Choose your target:")
        k = 0
        print(accuracy_list)
        while k < 1:
            for accuracy_place in accuracy_list[2]:
                print (type(Variables.board[accuracy_place[0]][accuracy_place[1]]))
                if target_character == Variables.board[accuracy_place[0]][accuracy_place[1]].name:
                    for i in range(int(1/chosen_weapon.dropoff)):
                        if ((character_coordinates(character)[0] - accuracy_place[0])**2 + (character_coordinates(character)[-1] - accuracy_place[1])**2)**0.5 <= chosen_weapon.range_+i:
                            k += 1
                            moves += 1
                            character.shoot = 1
                            if random.randint(0,100) < (100 - (chosen_weapon.dropoff * i * 100)):
                                deal_damage (character, chosen_weapon, Variables.board[accuracy_place[0]][accuracy_place[1]])
                                alive()
                            break
                        else:
                            print("The shot missed!")
                            break
                    if k < 1:
                        target_character = input("Choose a valid target:")
    else:
        print("No legal targets!")

    for accuracy_place in list1:
       placement_swap("_",int(accuracy_place[0]), int(accuracy_place[-1]))

    boardstate()
    return moves

def turn(character):
    desired_move = input("Do you want to move or shoot? (m=move or s=shoot)")
    boardstate()
    while 1 == 1:
        if desired_move == "m":
            moves = walk(character)
            break
        elif desired_move == "s":
            moves = shoot(character)
            break
        elif desired_move == "cancel":
            return 0
        else:
            desired_move = input("Choose a valid ability (m=move or s=shoot):")
    return moves

def deal_damage(shooter, weapon, target):
  target.health -= weapon.damage
  print(str(shooter)+" has dealt "+str(weapon.damage)+" damage to "+str(target)+"! "+str(target)+" has "+str(target.health)+" health left.")

def alive():
    living = Variables.characters_alive
    for character in Variables.characters_alive:
        if character.health <= 0:
            print("Character " + str(character) + " has died.")
            living.remove(character)
            for row in Variables.board:
                for place in row:
                    if place == character.name:
                        placement_swap("_", row.index(place), Variables.board.index(row))
    return living