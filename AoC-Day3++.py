def clear_row(triangle_to_split):
    triangle_to_split = triangle_to_split.split(" ")
    triangle_sides = []
    for i in triangle_to_split:
        if i != "":
            triangle_sides.append(int(i))
    print(triangle_sides)
    return triangle_sides


def is_triangle(triangle_sides):
    higest_side = max(triangle_sides)
    return sum(triangle_sides)>higest_side*2

def count_true_triangles(path_of_a_file):
    file = open(path_of_a_file, 'r')
    data = file.read()
    data = data.split("\n", len(data)-1)
    triangle_counter = 0
    column_1 = []
    column_2 = []
    column_3 = []
    for triangle in data:
        cleared_row = clear_row(triangle)
        column_1.append(cleared_row[0])
        column_2.append(cleared_row[1])
        column_3.append(cleared_row[2])
    for i in range(0,len(column_1),3):
        if is_triangle([column_1[i], column_1[i+1],column_1[i+2]]):
            triangle_counter += 1
    for i in range(0, len(column_2), 3):
        if is_triangle([column_2[i], column_2[i + 1], column_2[i + 2]]):
            triangle_counter += 1
    for i in range(0, len(column_3), 3):
        if is_triangle([column_3[i], column_3[i + 1], column_3[i + 2]]):
            triangle_counter += 1
    print(triangle_counter)


count_true_triangles("C:\\Users\\Poostaq\\Dysk Google\\Projekty\\Advent of Code\\day3 input")
