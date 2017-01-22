import collections
def decode_message(path_of_a_file):
    file = open(path_of_a_file, 'r')
    data = file.read()
    data = data.split("\n", len(data) - 1)
    characters_in_columns = ["","","","","","","","n"]
    common_characters = []
    password_characters = []

    for line in data:
        for i in range(0,len(line)):
            characters_in_columns[i] += line[i]
    for column in characters_in_columns:
        while len(column) > 0:
            common_characters.append(collections.Counter(column).most_common(1)[0])
            print(common_characters[len(common_characters)-1][0])
            column = column.replace(common_characters[len(common_characters)-1][0], "")
            print(column)
        password_characters.append(common_characters[len(common_characters)-1][0])

    print(password_characters)

decode_message("C:\\Users\\Poostaq\\Dysk Google\\Projekty\\Advent of Code\\day6 input")