def calculate_distance(string_with_steps):
    table_of_steps = string_with_steps.split(', ')
    actual_direction = 0
    table_of_directions = ["N", "E", "S", "W"]
    horizontal_coordinate = 0
    vertical_coordinate = 0
    number_from_i = 0
    table_of_visited_locations = []
    table_of_visited_locations.append([horizontal_coordinate, vertical_coordinate])
    sought_coordinates = []

    for i in table_of_steps:
        if "L" in i:
            if actual_direction == 0:
                actual_direction = 3
            else:
                actual_direction -= 1
            number_from_i = i.replace("L", "")
            print(number_from_i)
        else:
            if actual_direction == 3:
                actual_direction = 0
            else:
                actual_direction += 1
            number_from_i = i.replace("R", "")
            print(number_from_i)
        if table_of_directions[actual_direction] == "N":
            for i in range(0, int(number_from_i)):
                vertical_coordinate += 1
                # NIE CHCE MI SIĘ WYWALIC TEGO DO METODY
                if len(sought_coordinates) == 0:
                    for i in table_of_visited_locations:
                        if i == [horizontal_coordinate, vertical_coordinate]:
                            sought_coordinates = i
                table_of_visited_locations.append([horizontal_coordinate,vertical_coordinate])
            print("vertical distance = " + str(vertical_coordinate))
        elif table_of_directions[actual_direction] == "S":
            for i in range(0, int(number_from_i)):
                vertical_coordinate -= 1
                # NIE CHCE MI SIĘ WYWALIC TEGO DO METODY
                if len(sought_coordinates) == 0:
                    for i in table_of_visited_locations:
                        if i == [horizontal_coordinate, vertical_coordinate]:
                            sought_coordinates = i
                table_of_visited_locations.append([horizontal_coordinate,vertical_coordinate])
            print("vertical distance = " + str(vertical_coordinate))
        elif table_of_directions[actual_direction] == "E":
            for i in range(0, int(number_from_i)):
                horizontal_coordinate += 1
                # NIE CHCE MI SIĘ WYWALIC TEGO DO METODY
                if len(sought_coordinates) == 0:
                    for i in table_of_visited_locations:
                        if i == [horizontal_coordinate, vertical_coordinate]:
                            sought_coordinates = i
                table_of_visited_locations.append([horizontal_coordinate,vertical_coordinate])
            print("horizontal distance = " + str(horizontal_coordinate))
        else:
            for i in range(0, int(number_from_i)):
                horizontal_coordinate -= 1
                # NIE CHCE MI SIĘ WYWALIC TEGO DO METODY
                if len(sought_coordinates) == 0:
                    for i in table_of_visited_locations:
                        if i == [horizontal_coordinate, vertical_coordinate]:
                            sought_coordinates = i
                table_of_visited_locations.append([horizontal_coordinate,vertical_coordinate])
            print("horizontal distance = " + str(horizontal_coordinate))

    print(table_of_visited_locations)
    print(sought_coordinates)
calculate_distance("L4, R2, R4, L5, L3, L1, R4, R5, R1, R3, L3, L2, L2, R5, R1, L1, L2, R2, R2, L5, R5, R5, L2, R1, "
                   "R2, L2, L4, L1, R5, R2, R1, R1, L2, L3, R2, L5, L186, L5, L3, R3, L5, R4, R2, L5, R1, R4, L1, "
                   "L3, R3, R1, L1, R4, R2, L1, L4, R5, L1, R50, L4, R3, R78, R4, R2, L4, R3, L4, R4, L1, R5, L4, "
                   "R1, L2, R3, L2, R5, R5, L4, L1, L2, R185, L5, R2, R1, L3, R4, L5, R2, R4, L3, R4, L2, L5, R1, "
                   "R2, L2, L1, L2, R2, L2, R1, L5, L3, L4, L3, L4, L2, L5, L5, R2, L3, L4, R4, R4, R5, L4, L2, "
                   "R4, L5, R3, R1, L1, R3, L2, R2, R1, R5, L4, R5, L3, R2, R3, R1, R4, L4, R1, R3, L5, L1, L3, "
                   "R2, R1, R4, L4, R3, L3, R3, R2, L3, L3, R4, L2, R4, L3, L4, R5, R1, L1, R5, R3, R1, R3, R4, "
                   "L1, R4, R3, R1, L5, L5, L4, R4, R3, L2, R1, R5, L3, R4, R5, L4, L5, R2")