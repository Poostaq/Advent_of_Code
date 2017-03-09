index = 0


def get_input_from_file(path_of_a_file):
    opened_file = open(path_of_a_file, 'r')
    data = opened_file.read()
    return data
#OLD DATA
def count_length_of_file():
    data = get_input_from_file("C:\PRYWATNE\PROJEKTY\Advent_of_Code\day9 input")
    print(data)
    print(len(data))
    length_of_decompressed_file = 0
    while index != len(data):
        if data[index] == "(":
            index += 1
            marker = ""
            while data[index] != ")":
                marker += data[index]
                index += 1
            print(marker)
            marker = marker.split("x")
            length_of_decompressed_file += (int(marker[0])*int(marker[1]))
            index += int(marker[0]) + 1
        else:
            print(data[index])
            length_of_decompressed_file += 1
            index +=1
    print(length_of_decompressed_file)

#NEW DATA

def count_length_of_file_two():
    data = get_input_from_file("C:\PRYWATNE\PROJEKTY\Advent_of_Code\\day9 input")
    length_of_decompressed_file = evaluate_marker([len(data), 1], data)
    print(length_of_decompressed_file)


def evaluate_marker(marker_parameters, data):
    len_of_marker = int(marker_parameters[0])
    global index
    position_inside_marker = 0
    decompressed_length = 0
    while position_inside_marker < len_of_marker:
        print str(position_inside_marker) + " < " + str(len_of_marker)
        potential_marker = is_marker(data)
        if len(potential_marker) > 0:
            position_inside_marker += len(potential_marker)
            marker = potential_marker.strip("(").strip(")").split("x")
            value_of_marker = evaluate_marker(marker, data)
            decompressed_length += value_of_marker * int(marker[1])
            position_inside_marker += int(marker[0])
        else:
            index += 1
            position_inside_marker += 1
            decompressed_length += 1
    return decompressed_length


def is_marker(data):
    global index
    print "data[" + str(index) + "] = " + data[index]
    marker = ""
    if data[index] == "(":
        marker += data[index]
        index += 1
        while True:
            marker += data[index]
            if data[index] == ")":
                print "Marker to " + str(marker)
                break
            index += 1
        index += 1
    return marker

count_length_of_file_two()