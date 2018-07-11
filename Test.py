coordinates = [0, 0]

if delta_x == -1:
    coordinates[0] = coordinates[0] + place[0]

else:
    coordinates[0] = place[0]

if delta_y == -1:
    coordinates[-1] = coordinates[-1] + place[-1]

else:
    coordinates[-1] = place[-1]

if abs((coordinates[-1] - coordinates_origin[-1]) / (coordinates[0] - coordinates_origin[0])) < 1:
    for i in range(int((int(coordinates_origin[0] - coordinates[0]) ** 2 + int(
            coordinates_origin[-1] - coordinates[-1]) ** 2) ** 0.5)):
        if (coordinates[0] - delta_x * i) != coordinates_origin[0] or (coordinates[-1] - abs(
                (coordinates[-1] - coordinates_origin[-1]) / (coordinates[0] - coordinates_origin[0])) * i) != \
                coordinates_origin[-1]:
            if Variables.board[int(place[-1] - delta_y * abs(
                    (place[-1] - coordinates_origin[-1]) / (place[0] - coordinates_origin[0])) * i)][
                int(place[0] - delta_x * i)] != "_":
                for k in range(i):
                    different_targets(Variables.board[int(place[-1] - delta_y * abs(
                        (place[-1] - coordinates_origin[-1]) / (place[0] - coordinates_origin[0])) * k)][
                                          int(place[0] - delta_x * k)], illegal_list, int(place[0] - delta_x * k), int(
                        place[-1] - delta_y * abs(
                            (place[-1] - coordinates_origin[-1]) / (place[0] - coordinates_origin[0])) * k), target_1,
                                      target_2, other_characters)
                return
elif abs((coordinates[-1] - coordinates_origin[-1]) / (coordinates[0] - coordinates_origin[0])) >= 1:
    for i in range(int((int(coordinates_origin[-1] - coordinates[-1]) ** 2 + int(
            coordinates_origin[0] - coordinates[0]) ** 2) ** 0.5)):
        if (place[-1] - delta_y * i) != coordinates_origin[-1] or (place[0] - delta_x * abs(
                (place[0] - coordinates_origin[0]) / (place[-1] - coordinates_origin[-1])) * i) != coordinates_origin[
            0]:
            if Variables.board[int(place[-1] - delta_y * i)][int(place[0] - delta_x * abs(
                    (place[0] - coordinates_origin[0]) / (place[-1] - coordinates_origin[-1])) * i)] != "_":
                for k in range(i):
                    different_targets(Variables.board[int(place[-1] - delta_y * k)][int(place[0] - delta_x * abs(
                        (place[0] - coordinates_origin[0]) / (place[-1] - coordinates_origin[-1])) * k)], illegal_list,
                                      int(place[0] - delta_x * abs((place[0] - coordinates_origin[0]) / (
                                                  place[-1] - coordinates_origin[-1])) * k),
                                      int(place[-1] - delta_y * k), target_1, target_2, other_characters)
                return

        coordinates = [0, 0]

        if delta_x == -1:
            coordinates[0] = 2 * coordinates_origin[0] - place[0]

        else:
            coordinates[0] = place[0]

        if delta_y == -1:
            coordinates[-1] = 2 * coordinates_origin[-1] - place[-1]

        else:
            coordinates[-1] = place[-1]

        if abs((coordinates[-1] - coordinates_origin[-1]) / (coordinates[0] - coordinates_origin[0])) < 1:
            for i in range(int((int(coordinates_origin[0] - coordinates[0]) ** 2 + int(
                    coordinates_origin[-1] - coordinates[-1]) ** 2) ** 0.5)):
                if (coordinates[0] - delta_x * i) != coordinates_origin[0] or (coordinates[-1] - delta_x * abs(
                        (coordinates[-1] - coordinates_origin[-1]) / (coordinates[0] - coordinates_origin[0])) * i) != \
                        coordinates_origin[-1]:
                    if Variables.board[int(place[-1] - (1 + delta_y) / 2 * abs(
                            (place[-1] - coordinates_origin[-1]) / (place[0] - coordinates_origin[0]) * i + (
                                    1 - delta_y) / 2 * int(abs((coordinates[-1] - coordinates_origin[-1]) / (
                                    coordinates[0] - coordinates_origin[0]) * i))))][int(
                            place[0] - (1 + delta_x) / 2 * i + (1 - delta_x) / 2 * int(abs(
                                    (coordinates[-1] - coordinates_origin[-1]) / (
                                            coordinates[0] - coordinates_origin[0]) * i)))] != "_":
                        for k in range(i):
                            different_targets(Variables.board[int(place[-1] - (1 + delta_y) / 2 * abs(
                                (place[-1] - coordinates_origin[-1]) / (place[0] - coordinates_origin[0]) * k + (
                                            1 - delta_y) / 2 * int(abs(
                                    (place[-1] - coordinates_origin[-1]) / (place[0] - coordinates_origin[0]) * k))))][
                                                  int(place[0] - (1 + delta_x) / 2 * k + (1 - delta_x) / 2 * int(abs(
                                                      (coordinates[-1] - coordinates_origin[-1]) / (
                                                                  coordinates[0] - coordinates_origin[0]) * k)))],
                                              illegal_list, int(
                                    place[0] - (1 + delta_x) / 2 * k + (1 - delta_x) / 2 * int(abs(
                                        (coordinates[-1] - coordinates_origin[-1]) / (
                                                    coordinates[0] - coordinates_origin[0]) * k))), int(
                                    place[-1] - (1 + delta_y) / 2 * abs((place[-1] - coordinates_origin[-1]) / (
                                                place[0] - coordinates_origin[0])) * i + (1 - delta_y) / 2 * int(abs(
                                        (coordinates[-1] - coordinates_origin[-1]) / (
                                                    coordinates[0] - coordinates_origin[0]) * k))), target_1, target_2,
                                              other_characters)
                        return
        elif abs((coordinates[-1] - coordinates_origin[-1]) / (coordinates[0] - coordinates_origin[0])) >= 1:
            for i in range(int((int(coordinates_origin[-1] - coordinates[-1]) ** 2 + int(
                    coordinates_origin[0] - coordinates[0]) ** 2) ** 0.5)):
                if (coordinates[-1] - delta_y * i) != coordinates_origin[-1] or (coordinates[0] - delta_x * abs(
                        (coordinates[0] - coordinates_origin[0]) / (coordinates[-1] - coordinates_origin[-1])) * i) != \
                        coordinates_origin[0]:
                    if Variables.board[int(place[-1] - (1 + delta_y) / 2 * i + (1 - delta_y) / 2 * int(abs(
                            (coordinates[-1] - coordinates_origin[-1]) / (
                                    coordinates[0] - coordinates_origin[0]) * i)))][int(
                            place[0] - (1 + delta_x) / 2 * abs((coordinates[0] - coordinates_origin[0]) / (
                                    coordinates[-1] - coordinates_origin[-1]) * i + (1 - delta_x) / 2 * int(abs(
                                    (coordinates[0] - coordinates_origin[0]) / (
                                            coordinates[-1] - coordinates_origin[-1]) * i))))] != "_":
                        for k in range(i):
                            different_targets(Variables.board[int(
                                place[-1] - (1 + delta_y) / 2 * k + (1 - delta_y) / 2 * int(abs(
                                    (coordinates[-1] - coordinates_origin[-1]) / (
                                                coordinates[0] - coordinates_origin[0]) * i)))][int(
                                place[0] - (1 + delta_x) / 2 * abs(
                                    (place[0] - coordinates_origin[0]) / (place[-1] - coordinates_origin[-1]) * k + (
                                                1 - delta_x) / 2 * int(abs((coordinates[0] - coordinates_origin[0]) / (
                                                coordinates[-1] - coordinates_origin[-1]) * i))))], illegal_list, int(
                                place[0] - (1 + delta_x) / 2 * abs(
                                    (place[0] - coordinates_origin[0]) / (place[-1] - coordinates_origin[-1]) * k + (
                                                1 - delta_x) / 2 * int(abs((coordinates[0] - coordinates_origin[0]) / (
                                                coordinates[-1] - coordinates_origin[-1]) * i)))), int(
                                place[-1] - (1 + delta_y) / 2 * k + (1 - delta_y) / 2 * int(abs(
                                    (coordinates[-1] - coordinates_origin[-1]) / (
                                                coordinates[0] - coordinates_origin[0]) * i))), target_1, target_2,
                                              other_characters)
                        return


    if abs((coordinates[-1] - coordinates_origin[-1]) / (coordinates[0] - coordinates_origin[0])) < 1:
        for i in range(int((int(coordinates_origin[0] - coordinates[0]) ** 2 + int(coordinates_origin[-1] - coordinates[-1]) ** 2) ** 0.5)):
            if (coordinates[0] - delta_x * i) != coordinates_origin[0] or int(coordinates[-1] - (1 + delta_y)/2 * math.floor(abs((coordinates[-1] - coordinates_origin[-1]) / (coordinates[0] - coordinates_origin[0])) * i) + (1 - delta_y)/2 * math.ceil(abs((coordinates[-1] - coordinates_origin[-1]) / (coordinates[0] - coordinates_origin[0])) * i)) != coordinates_origin[-1]:
                if Variables.board[int(coordinates[-1] - (1 + delta_y)/2 * math.floor(abs((coordinates[-1] - coordinates_origin[-1]) / (coordinates[0] - coordinates_origin[0])) * i) + (1 - delta_y)/2 * math.ceil(abs((coordinates[-1] - coordinates_origin[-1]) / (coordinates[0] - coordinates_origin[0])) * i))][int(coordinates[0] - delta_x * i)] != "_":
                    for k in range(i):
                        different_targets(Variables.board[int(coordinates[-1] - (1 + delta_y)/2 * math.floor(abs((coordinates[-1] - coordinates_origin[-1]) / (coordinates[0] - coordinates_origin[0])) * k) + (1 - delta_y)/2 * math.ceil(abs((coordinates[-1] - coordinates_origin[-1]) / (coordinates[0] - coordinates_origin[0])) * k))][int(coordinates[0] - delta_x * k)], illegal_list, int(coordinates[0] - delta_x * k),
                                          int(coordinates[-1] - (1 + delta_y) / 2 * math.floor(abs((coordinates[-1] - coordinates_origin[-1]) / (coordinates[0] - coordinates_origin[0])) * k) + (1 - delta_y) / 2 * math.ceil(abs((coordinates[-1] - coordinates_origin[-1]) / (coordinates[0] - coordinates_origin[0])) * k)), target_1, target_2, other_characters)
                    return
    elif abs((coordinates[-1] - coordinates_origin[-1]) / (coordinates[0] - coordinates_origin[0])) >= 1:
        for i in range(int((int(coordinates_origin[-1] - coordinates[-1]) ** 2 + int(coordinates_origin[0] - coordinates[0]) ** 2) ** 0.5)):
            if int(coordinates[-1] - delta_y * i) != coordinates_origin[-1] or int(coordinates[0] - (1 + delta_x)/2 * math.floor(abs((coordinates[0] - coordinates_origin[0]) / (coordinates[-1] - coordinates_origin[-1])) * i) + (1 - delta_x)/2 * math.ceil(abs((coordinates[0] - coordinates_origin[0]) / (coordinates[-1] - coordinates_origin[-1])) * i)) != coordinates_origin[0]:
                if Variables.board[int(coordinates[-1] - delta_y * i)][int(coordinates[0] - (1 + delta_x)/2 * int(abs((coordinates[0] - coordinates_origin[0]) / (coordinates[-1] - coordinates_origin[-1])) * i) + (1 - delta_x)/2 * math.ceil(abs((coordinates[0] - coordinates_origin[0]) / (coordinates[-1] - coordinates_origin[-1])) * i))] != "_":
                    for k in range(i):
                        different_targets(Variables.board[int(coordinates[-1] - delta_y * i)][int(coordinates[0] - (1 + delta_x)/2 * math.floor(abs((coordinates[0] - coordinates_origin[0]) / (coordinates[-1] - coordinates_origin[-1])) * k) + (1 - delta_x)/2 * math.ceil(abs((coordinates[0] - coordinates_origin[0]) / (coordinates[-1] - coordinates_origin[-1])) * k))], illegal_list,
                                          int(coordinates[0] - (1 + delta_x) / 2 * math.floor(abs((coordinates[0] - coordinates_origin[0]) / (coordinates[-1] - coordinates_origin[-1])) * k) + (1 - delta_x) / 2 * math.ceil(abs((coordinates[0] - coordinates_origin[0]) / (coordinates[-1] - coordinates_origin[-1])) * k)), (coordinates[-1] - delta_y * k), target_1, target_2, other_characters)
                    return

    if abs((coordinates[-1] - coordinates_origin[-1]) / (coordinates[0] - coordinates_origin[0])) < 1:
        for i in range(int((int(coordinates_origin[0] - coordinates[0]) ** 2 + int(coordinates_origin[-1] - coordinates[-1]) ** 2) ** 0.5)):
            if (coordinates[0] - delta_x * i) != coordinates_origin[0] or int(coordinates[-1] - delta_y * round(abs((coordinates[-1] - coordinates_origin[-1]) / (coordinates[0] - coordinates_origin[0])) * i)) != coordinates_origin[-1]:
                if Variables.board[int(coordinates[-1] - delta_y * round(abs((coordinates[-1] - coordinates_origin[-1]) / (coordinates[0] - coordinates_origin[0])) * i))][int(coordinates[0] - delta_x * i)] != "_":
                    for k in range(i):
                        different_targets(Variables.board[int(coordinates[-1] - delta_y * round(abs((coordinates[-1] - coordinates_origin[-1]) / (coordinates[0] - coordinates_origin[0])) * k))][int(coordinates[0] - delta_x * k)], illegal_list, int(coordinates[0] - delta_x * k),
                                          int(coordinates[-1] - delta_y * round(abs((coordinates[-1] - coordinates_origin[-1]) / (coordinates[0] - coordinates_origin[0])) * k)), target_1, target_2, other_characters)
                    return
    elif abs((coordinates[-1] - coordinates_origin[-1]) / (coordinates[0] - coordinates_origin[0])) >= 1:
        for i in range(int((int(coordinates_origin[-1] - coordinates[-1]) ** 2 + int(coordinates_origin[0] - coordinates[0]) ** 2) ** 0.5)):
            if int(coordinates[-1] - delta_y * i) != coordinates_origin[-1] or int(coordinates[0] - delta_x * round(abs((coordinates[0] - coordinates_origin[0]) / (coordinates[-1] - coordinates_origin[-1])) * i)) != coordinates_origin[0]:
                if Variables.board[int(coordinates[-1] - delta_y * i)][int(coordinates[0] - delta_x * round(abs((coordinates[0] - coordinates_origin[0]) / (coordinates[-1] - coordinates_origin[-1])) * i))] != "_":
                    for k in range(i):
                        different_targets(Variables.board[int(coordinates[-1] - delta_y * i)][int(coordinates[0] - delta_x * round(abs((coordinates[0] - coordinates_origin[0]) / (coordinates[-1] - coordinates_origin[-1])) * k))], illegal_list,
                                          int(coordinates[0] - delta_x * round(abs((coordinates[0] - coordinates_origin[0]) / (coordinates[-1] - coordinates_origin[-1])) * k)), (coordinates[-1] - delta_y * k), target_1, target_2, other_characters)
                    return