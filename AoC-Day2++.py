def bathroom_code_digit(line_of_code, starting_horizontal_coordinate, starting_vertical_coordinate):

    keypad = [["", "", 1, "", ""],
              ["", 2, 3, 4, ""],
              [5, 6, 7, 8, 9],
              ["", "A", "B", "C", ""],
              ["", "", "D", "", ""]]

    for i in range(0,len(line_of_code)):
        if line_of_code[i] == "U":
            if starting_horizontal_coordinate != 0 and keypad[starting_horizontal_coordinate-1][starting_vertical_coordinate] != "":
                starting_horizontal_coordinate -= 1
        if line_of_code[i] == "R":
            if starting_vertical_coordinate != 4 and keypad[starting_horizontal_coordinate][starting_vertical_coordinate+1] != "":
                starting_vertical_coordinate += 1
        if line_of_code[i] == "D":
            if starting_horizontal_coordinate != 4 and keypad[starting_horizontal_coordinate+1][starting_vertical_coordinate] != "":
                starting_horizontal_coordinate += 1
        if line_of_code[i] == "L":
            if starting_vertical_coordinate != 0 and keypad[starting_horizontal_coordinate][starting_vertical_coordinate-1] != "":
                starting_vertical_coordinate -= 1
    print(str(starting_horizontal_coordinate) + ", " + str(starting_vertical_coordinate))
    return [starting_horizontal_coordinate, starting_vertical_coordinate]

def generate_code():
    keypad = [["", "", 1, "", ""],
              ["", 2, 3, 4, ""],
              [5, 6, 7, 8, 9],
              ["", "A", "B", "C", ""],
              ["", "", "D", "", ""]]
    code = []
    horizontal_coordinate = 3
    vertical_coordinate = 0
    coordinates = bathroom_code_digit(
        "RUDULRLLUULRURDDRRUDURULLLDRLRLUDDLUDUDDUDRRDUDULDUUULLRULLRLDDLDLDDRLRRRRUDLLDDUULDRLLUDDRRUURLU"
        "LRRRDLLURRUUDURUDDURLUDDDLUDDUUDUURUDLRDRDRLRDRLDRUDRUUDLRDDRRURDDLRDDRRURDUDDLULLUDRURURRRLRRUDU"
        "ULULULRRLDLUDUURRLLRUDLLDRDDLRRRULRUDLULDDLLLULDLRUDLLLLRDDLRDRLDRLLRDRRDLRDULULRLLLDRUDRRRUULRUU"
        "LDRURLUDRURRDLLDLRDLDDDDRRLUDLRRLUUUURDRDDLRRURURRDUULLRLURLURUDDDRDURDUUDRLRLRRLDDLDLDLDDDUDDULU"
        "RLDDLLRLRRDULUDDLULRLUDDLDLRULUUUDRLDRUDURLUDDRLLRUULDLRRRRDLLLLURULLRDRRUDLUULRRDLLRLRLUDLDDULLD"
        "LLRDLDLL", horizontal_coordinate, vertical_coordinate)
    code.append(keypad[coordinates[0]][coordinates[1]])
    coordinates = bathroom_code_digit(
        "LLUUUUUUDUDRLRDRDLDURRRLLRRLRURLLUURRLLUDUDLULUURUUURDLUDLDDLULLRDLRUULDLRDUDURLLDDUDUDULLUDDUULL"
        "LUULRRRLULRURRDLRUDUDDURRRDRUURDURLLULLRULLDRUULLURLDRDUUDDDDDDRRLDRLRRRLULDDUURRLLLLDRURLURDRDRD"
        "URUDUURRDUDUDRLLUUDDRLUDDDRDLDLRLDRURRDLLRULDRLLURURRLUULLRLRRURDDRDRUUURUURUUUDLLRRLUDRLDLRLURLD"
        "LUDDUDDDLDUDRRLDLRURULRLLRDUULURRRULDLLLRLDDDUURRRRDULLRURRLULULDLRRUDUDDLRUURDLDUDDUDRRDLRRRDUDU"
        "UUDLLDDDDLURLURRRUUULLLULRRLLLLLLULDUUDLRUDRRDLRDUUDUDLLRLDLLRUURDUUURUUUDDLLUUDLULDURLULULUUUDRU"
        "DULLURRULRULLRDLDDU", horizontal_coordinate, vertical_coordinate)
    code.append(keypad[coordinates[0]][coordinates[1]])
    coordinates = bathroom_code_digit(
        "RLUUURULLDLRLDUDRDURRDUURLLUDDDUULRRRLRLURDDRUULUDULDUUDDDDUDDDDRUDDLDUUDRUDLRRRLLRDDLLLRLLRUULRU"
        "ULDDRURRLURRLRLULDDRRRDDURDDRDRDULRUDRUUDULRLLULDLRLLDRULRDDRRDDUDLRLLUDRDRRRLUDULRDLRDDURRUUDDRR"
        "UDURRUUUDDRRDUDURLUUDUDUURDDDLURLULLUULULURUDUUDRUDULLUUULURDLDUULLDDLLDULRLRLRDUUURUUDLRLDURUDRL"
        "DULLUDLDLLRDUURRDUDURLUUUDLLRRULRLULRLDLLURDURRULRLLRRDUDLLRDRRRRDLUUDRUUUDDLRLUDDDDDDRURRRUUURRD"
        "LLRURLDDLLDLRRLLLDRRULRRUDLDRDDRRLULURLLUURURURRRRUUUUURUDURLRLLLULULDLLDLRDRRULUDUDRDRRDRDRRDUDL"
        "LLRUDRUDDDULRULRRRDRLRUUUURUDURDUUULLULRUDDULDUUDLDURRD", horizontal_coordinate, vertical_coordinate)
    code.append(keypad[coordinates[0]][coordinates[1]])
    coordinates = bathroom_code_digit(
        "ULRULDDLDLULLLRRRLRUDDDDDLLDDUDLRRDULUUDRDLRRURDRRLUULRURUDRRULDLLLUDRUUDULULUDDRUDDDRDURRRDRDUUU"
        "RLRDULUDRDRLDRUDDLLLDRRULUDLUDLDLLRRUDUULULDLDLLUURDLDDLLUUDURLURLLLDRDLDRRLRULUURRDRULRUUURULRRU"
        "DDDDLLDLDDLLRRLRRRRDUUDUDLDRDRRURDLRURULDLRDLLLLRUDRLLRDLRLRDURDRUDURRRLRDRDLLRLUDDDDRLRLLDUURRUR"
        "LUURUULUDLUURDRRUDDLUDUDDDURRDRUDRLRULDULUUUUUUDDUDRUDUUURUDRRDLUDLUUDUULUDURDLDDDLLURRURUUDUDDRR"
        "DRLLULULDRLRURRDDDRDUUURDDDRULUDRDDLDURRLDDDLRRRLDDRDURULDLUDLLLURLURRLRRULDLLDDUDRRULDRRRRLURRUU"
        "LRRRUDLURDLLDLLDULUUDRRLDLLLDRLRUDLUULDLDRUDUDURDRUDRDDDLRLULLUR", horizontal_coordinate, vertical_coordinate)
    code.append(keypad[coordinates[0]][coordinates[1]])
    coordinates = bathroom_code_digit(
        "LRLUUURRLRRRRRUURRLLULRLULLDLUDLUDRDDRLDLRLULLURDURLURDLLRLDUUDDURRRRLDLLRULLRLDLLUUDRLDDLLDRULDR"
        "LLRURDLRURRUDLULLRURDLURRURUDULLDRLLUUULUDRURRUUDUDULUUULRLDDULDRDLUDDUDDDLRURULLDLLLRLLUURDLRUDL"
        "LLLDLLRLRUUUDDRUUUUDLDLRDDURLDURUULLLUUDLLLLDULRRRLLDLDRRDRLUDRUDURLLUDLRLLUDUDRDDDRDLRDLRULUULDR"
        "LUDLRLDUURLRRLUDDDUUDDDUDRLDLDUDLURUULLDDDURUUULRLUDLDURUUDRDRURUDDUURDUUUDLLDLDLDURUURLLLLRURUUR"
        "URULRULLRUDLRRUUUUUDRRLLRDDUURDRDRDDDUDRLURDRRRUDLLLDURDLUUDLLUDDULUUDLDUUULLDRDLRURUURRDURRDLURR"
        "RRLLUUULRDULDDLDUURRDLDLLULRRLLUDLDUDLUUL", horizontal_coordinate, vertical_coordinate)
    code.append(keypad[coordinates[0]][coordinates[1]])
    print(code)

generate_code()